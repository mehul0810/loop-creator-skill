# Loop Creator Skill

`loop-creator` interviews a user, inspects their business and AI-tool setup, researches current version-specific capabilities, and designs a token-efficient autonomous operating loop with approval gates for critical actions.

It supports:

- solopreneur, single-product, multi-product portfolio, and organization structures;
- approximately 90–95% autonomous routine execution;
- dynamic event/schedule cadence and quiet no-change behavior;
- version-aware model and reasoning routing;
- per-run, product, period, and portfolio token/cost budgets;
- independent verification, compact state, stop rules, and human approval packets.

## Repository structure

```text
loop-creator/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── LOOP.md.template
│   ├── first-run-prompt.md.template
│   ├── recommendation.md.template
│   └── run-note.md.template
└── references/
    ├── business-topologies.md
    ├── discovery-interview.md
    ├── dynamic-cadence.md
    ├── model-routing-and-token-efficiency.md
    ├── patterns.md
    ├── research-notes.md
    ├── setup-canvas.md
    ├── tool-version-research.md
    └── verification.md
```

The hot path stays in `SKILL.md`. Detailed guidance loads selectively from `references/`, while reusable output templates live in `assets/`.

## Install

Clone the repository, then point each filesystem-based agent at the same skill directory.

### Codex

```bash
mkdir -p ~/.codex/skills
ln -s "/absolute/path/to/loop-creator-skill/loop-creator" ~/.codex/skills/loop-creator
```

Restart Codex if the skill does not appear in an existing session.

### Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s "/absolute/path/to/loop-creator-skill/loop-creator" ~/.claude/skills/loop-creator
```

Claude Code supports personal skills under `~/.claude/skills/` and watches existing skill directories for changes.

### ChatGPT

ChatGPT custom skills are installed through the ChatGPT interface and do not currently sync from Codex or a local filesystem directory.

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

## Contributing

Read `AGENTS.md` before changing the repository. Keep `SKILL.md` compact, place detailed material in directly linked references, avoid duplicate guidance, and validate every meaningful change.

## License

MIT. See `LICENSE`.
