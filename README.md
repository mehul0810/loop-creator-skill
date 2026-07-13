# Loop Creator Skill

`loop-creator` interviews a user, inspects their business and AI-tool setup, researches current version-specific capabilities, and designs a token-efficient autonomous operating loop with approval gates for critical actions.

It supports:

- solopreneur, single-product, multi-product portfolio, and organization structures;
- approximately 90–95% autonomous routine execution;
- dynamic event/schedule cadence and quiet no-change behavior;
- version-aware model and reasoning routing;
- per-run, product, period, and portfolio token/cost budgets;
- independent verification, compact state, stop rules, and human approval packets.
- a canonical extensible state schema, measurable autonomy, trust boundaries, and loop lifecycle controls;
- a checksummed schema manifest so runtimes can detect copied-contract drift before they rely on it;
- concrete approval/cadence adapters, worked examples, and deterministic contract validation.

## Repository structure

```text
loop-creator/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── LOOP.md.template
│   ├── first-run-prompt.md.template
│   ├── loop-state.example.json
│   ├── loop-state.schema.json
│   ├── recommendation.md.template
│   └── run-note.md.template
├── examples/
│   ├── ci-triage-loop.md
│   ├── portfolio-loop.md
│   └── solopreneur-content-loop.md
├── scripts/
│   └── validate_loop.py
└── references/
    ├── approval-and-cadence-recipes.md
    ├── business-topologies.md
    ├── discovery-interview.md
    ├── dynamic-cadence.md
    ├── model-routing-and-token-efficiency.md
    ├── patterns.md
    ├── research-notes.md
    ├── security-and-trust.md
    ├── setup-canvas.md
    ├── state-autonomy-and-lifecycle.md
    ├── tool-version-research.md
    └── verification.md
```

The hot path stays in `SKILL.md`. Detailed guidance loads selectively from `references/`, while reusable output templates live in `assets/`.

## Install

Clone the repository, then point each filesystem-based agent at the same skill directory.

### ChatGPT desktop app and Codex

```bash
mkdir -p ~/.agents/skills
ln -s "/absolute/path/to/loop-creator-skill/loop-creator" ~/.agents/skills/loop-creator
```

Current Codex versions discover personal skills from `~/.agents/skills/` and support symlinked skill directories. In the ChatGPT desktop app, open **Skills** in the sidebar to find local skills. Restart the app if a newly installed skill does not appear.

### Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s "/absolute/path/to/loop-creator-skill/loop-creator" ~/.claude/skills/loop-creator
```

Claude Code supports personal skills under `~/.claude/skills/` and watches existing skill directories for changes.

### ChatGPT web and workspace installation

ChatGPT web/workspace custom skills are installed through the ChatGPT interface and do not currently sync from the local Codex installation.

1. Create a ZIP archive whose top-level directory is `loop-creator/`.
2. In ChatGPT, open profile → **Skills** → **New skill** → **Upload from your computer**.
3. Upload the ZIP and review the skill scan result before installing it.

Skill availability and upload permissions depend on the ChatGPT plan and workspace settings. See [Skills in ChatGPT](https://help.openai.com/en/articles/20001066).

## Use

Invoke it explicitly when desired:

```text
Use $loop-creator to interview me and design an autonomous loop for my business.
```

Example requests:

- “Create a quiet operating loop for my solopreneur SaaS and consulting business.”
- “Design product loops plus a portfolio loop for our four software products.”
- “Adapt this support workflow to my installed Claude Code version.”
- “Reduce token cost by routing routine and critical tasks to different model classes.”

The skill first inspects discoverable context, then asks no more than five short questions at a time. It verifies current tool/version behavior before producing a recommendation.

## Validate

Use the validator bundled with Codex Skill Creator:

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" loop-creator
```

The expected result is `Skill is valid!`.

The canonical state schema is `loop-creator/assets/loop-state.schema.json`. Its adjacent `schema-manifest.json` pins the schema version and checksum; downstream runtimes should record that provenance and fail validation when it drifts.

Validate a filled contract and optional JSON state:

```bash
python3 loop-creator/scripts/validate_loop.py path/to/LOOP.md --state path/to/state.json
```

Run the repository regression suite:

```bash
python3 -m unittest discover -s tests -v
```

## Contributing

Read `AGENTS.md` before changing the repository. Keep `SKILL.md` compact, place detailed material in directly linked references, avoid duplicate guidance, and validate every meaningful change.

## License

MIT. See `LICENSE`.
