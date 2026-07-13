#!/usr/bin/env python3
"""Validate a Loop Creator contract and optional JSON state without dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


REQUIRED_HEADINGS = (
    "Purpose",
    "Trust boundaries",
    "Verification",
    "State and observability",
    "Limits and exits",
    "Authority",
    "Lifecycle",
)

REQUIRED_FIELDS = (
    "Outcome",
    "Owner",
    "Autonomy target",
    "Autonomy measure",
    "Instruction authorities",
    "Untrusted data",
    "Injection response",
    "Required checks",
    "Passing condition",
    "State location",
    "State format / schema",
    "Iteration cap",
    "Time/token/cost cap",
    "Automatic",
    "Require approval",
    "Never automatic",
    "Approval packet",
    "Pause / resume",
    "Kill switch",
    "Promotion",
    "Demotion / pause",
    "Review cadence",
    "Retirement",
)

TERMINAL_TERMS = ("Success", "No-op", "Blocked", "Failed", "Escalate")
PLACEHOLDER_RE = re.compile(
    r"(?:^#+\s*|^\s*-\s+\*\*[^*]+:\*\*\s*|^\s*\d+\.\s+)(\[[^\]\n]+\])\s*$",
    flags=re.MULTILINE,
)


def contract_errors(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
    if placeholders:
        preview = ", ".join(placeholders[:5])
        errors.append(f"unfilled bracket placeholders: {preview}")

    headings = set(re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE))
    for heading in REQUIRED_HEADINGS:
        if heading not in headings:
            errors.append(f"missing required heading: {heading}")

    for field in REQUIRED_FIELDS:
        match = re.search(rf"^\s*-\s+\*\*{re.escape(field)}:\*\*\s*(.+?)\s*$", text, flags=re.MULTILINE)
        if not match:
            errors.append(f"missing required field: {field}")
        elif not match.group(1).strip():
            errors.append(f"empty required field: {field}")

    for term in TERMINAL_TERMS:
        if not re.search(rf"^\s*-\s+\*\*{re.escape(term)}:\*\*\s*\S", text, flags=re.MULTILINE):
            errors.append(f"missing terminal-state definition: {term}")

    if re.search(r"\*\*(Iteration cap|Time/token/cost cap):\*\*\s*(?:not measured|none|unlimited)\b", text, flags=re.IGNORECASE):
        errors.append("iteration and time/token/cost caps must be explicit and bounded")

    return errors


def type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    return True


def schema_errors(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if expected:
        expected_types = expected if isinstance(expected, list) else [expected]
        if not any(type_matches(value, item) for item in expected_types):
            return [f"{path}: expected {' or '.join(expected_types)}"]

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: must be one of {schema['enum']}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than {schema['minLength']}")
        if schema.get("format") == "date-time" and value:
            try:
                datetime.fromisoformat(value.replace("Z", "+00:00"))
            except ValueError:
                errors.append(f"{path}: invalid ISO 8601 date-time")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: must be >= {schema['minimum']}")
    if isinstance(value, list):
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: has more than {schema['maxItems']} items")
        if "items" in schema:
            for index, item in enumerate(value):
                errors.extend(schema_errors(item, schema["items"], f"{path}[{index}]"))
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required key {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in properties:
                    errors.append(f"{path}: unexpected key {key!r}")
        for key, child in properties.items():
            if key in value:
                errors.extend(schema_errors(value[key], child, f"{path}.{key}"))
    return errors


def state_errors(path: Path, schema_path: Path) -> list[str]:
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"]
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    return schema_errors(state, schema)


def schema_manifest_errors(schema_path: Path) -> list[str]:
    manifest_path = schema_path.with_name("schema-manifest.json")
    if not manifest_path.is_file():
        return [f"schema manifest not found: {manifest_path}"]
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"schema manifest has invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"]

    errors: list[str] = []
    expected_path = "loop-creator/assets/loop-state.schema.json"
    if manifest.get("schema_name") != "loop-state":
        errors.append("schema manifest must name loop-state")
    if manifest.get("schema_version") != "1.0":
        errors.append("schema manifest schema_version must be 1.0")
    if manifest.get("path") != expected_path:
        errors.append(f"schema manifest path must be {expected_path}")
    digest = hashlib.sha256(schema_path.read_bytes()).hexdigest()
    if manifest.get("sha256") != digest:
        errors.append("schema manifest checksum does not match the schema")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path, help="Filled LOOP.md contract")
    parser.add_argument("--state", type=Path, help="Optional JSON state file")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "assets" / "loop-state.schema.json",
        help="State schema path",
    )
    args = parser.parse_args()

    checks: list[tuple[str, list[str]]] = []
    if not args.contract.is_file():
        print(f"ERROR contract not found: {args.contract}", file=sys.stderr)
        return 2
    if not args.schema.is_file():
        print(f"ERROR schema not found: {args.schema}", file=sys.stderr)
        return 2
    manifest_errors = schema_manifest_errors(args.schema)
    if manifest_errors:
        print("FAIL schema manifest")
        for error in manifest_errors:
            print(f"  - {error}")
        return 1
    checks.append((str(args.contract), contract_errors(args.contract)))

    if args.state:
        if not args.state.is_file():
            print(f"ERROR state not found: {args.state}", file=sys.stderr)
            return 2
        checks.append((str(args.state), state_errors(args.state, args.schema)))

    failed = False
    for label, errors in checks:
        if errors:
            failed = True
            print(f"FAIL {label}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {label}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
