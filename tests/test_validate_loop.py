import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "loop-creator" / "scripts" / "validate_loop.py"
FIXTURES = ROOT / "tests" / "fixtures"


class ValidateLoopTests(unittest.TestCase):
    def run_validator(self, fixture: str) -> subprocess.CompletedProcess[str]:
        folder = FIXTURES / fixture
        state = folder / "state.json"
        if not state.exists():
            state = ROOT / "loop-creator" / "assets" / "loop-state.example.json"
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(folder / "LOOP.md"), "--state", str(state)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_valid_contract_and_state_pass(self) -> None:
        result = self.run_validator("valid")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.count("PASS "), 2)

    def test_invalid_contract_and_state_fail_with_actionable_errors(self) -> None:
        result = self.run_validator("invalid")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("unfilled bracket placeholders", result.stdout)
        self.assertIn("missing required heading: Trust boundaries", result.stdout)
        self.assertIn("missing required key 'updated_at'", result.stdout)
        self.assertIn("unexpected key 'unexpected'", result.stdout)

    def test_bundled_examples_are_complete_contracts(self) -> None:
        examples = ROOT / "loop-creator" / "examples"
        for contract in sorted(examples.glob("*.md")):
            with self.subTest(contract=contract.name):
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), str(contract)],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_schema_manifest_matches_the_canonical_contract(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(FIXTURES / "valid" / "LOOP.md")],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("FAIL schema manifest", result.stdout)


if __name__ == "__main__":
    unittest.main()
