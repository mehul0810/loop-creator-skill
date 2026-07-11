# Loop Creator Repository Guide

Use this repository as the source of truth for the `loop-creator` Agent Skill.

## Start every change

1. Run `git status --short --branch` and preserve unrelated work.
2. Read `loop-creator/SKILL.md` and only the references relevant to the request.
3. Inspect current official documentation before changing tool-, model-, permission-, pricing-, or version-specific guidance.
4. Keep repository documentation separate from runtime skill content.

## Skill structure

- `loop-creator/SKILL.md` is the compact execution kernel and must remain under 500 lines.
- `loop-creator/agents/openai.yaml` contains generated UI metadata and must stay aligned with `SKILL.md`.
- `loop-creator/references/` contains detailed guidance loaded selectively. Link every reference directly from `SKILL.md`; avoid reference-to-reference dependency chains.
- `loop-creator/assets/` contains templates copied or adapted into user deliverables. Do not use assets for explanatory documentation.
- Add `scripts/` only when deterministic repeated execution justifies code. Test every added script.

Do not add `README.md`, `DESIGN.md`, `CHANGELOG.md`, installation guides, or quick-reference files inside `loop-creator/`. Repository-facing documentation belongs at the repository root.

## Content rules

- Write skill instructions in imperative form.
- Keep the workflow business- and setup-specific rather than prescribing one universal loop.
- Preserve the default target of high routine autonomy with approval for destructive, irreversible, externally visible, sensitive, expensive, or authority-expanding actions.
- Keep model names, reasoning controls, prices, credits, feature flags, and installation paths version-aware and sourced from current official documentation.
- Prefer event triggers, adaptive cadence, compact state, focused context bundles, bounded fallback chains, and measurable verification.
- Do not duplicate content between `SKILL.md`, references, assets, and root documentation.
- Do not add a new architectural layer, agent role, or document unless it makes a real decision or eliminates repeated work.

## Validation

Run:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" loop-creator
python3 -m unittest discover -s tests -v
python3 loop-creator/scripts/validate_loop.py tests/fixtures/valid/LOOP.md --state tests/fixtures/valid/state.json
git diff --check
```

Also verify:

- every `references/...` and `assets/...` link from `SKILL.md` exists;
- `agents/openai.yaml` still describes the current skill;
- no placeholder `TODO` text remains;
- new operational claims include dated primary sources;
- meaningful changes have a representative forward-test when safe.
- every new or changed state field remains compatible with `assets/loop-state.schema.json` or includes an explicit schema migration;
- security-sensitive changes retain untrusted-input, approval-boundary, and kill-switch regression coverage.

## Git and publishing

- Commit only the intended repository files.
- Do not push, tag, publish a release, or alter installation symlinks unless the user explicitly asks.
- Treat the ChatGPT desktop/Codex installation at `~/.agents/skills/loop-creator` and the Claude installation at `~/.claude/skills/loop-creator` as symlinks to `loop-creator/`; do not copy divergent versions into those directories.
- ChatGPT web/workspace skills are uploaded through the product UI and do not currently sync from the local filesystem installation.
