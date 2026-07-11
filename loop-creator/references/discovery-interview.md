# Discovery interview

Interview to understand the business, operating topology, workflow, user taste, and approval boundary before recommending an architecture. Inspect first, ask second, and stop interviewing when the remaining uncertainty would not change the design.

## Express path

For one bounded workflow with a clear owner and existing work/proof surfaces, inspect first and ask at most three questions: desired outcome, consequential approval boundary, and any business or taste choice that materially changes the design. State inferred defaults for cadence, communication, state, and cost instead of interviewing dimension by dimension. Expand to the full interview only when unresolved topology, authority, risk, or implementation constraints require it.

## Full first question batch

Ask no more than five questions at once:

1. **Business and topology:** Are you a solopreneur, product team, multi-product portfolio, department, or organization? What do you sell or operate, and how does the work create value?
2. **Outcome:** What should this loop accomplish, and what is one representative input and desired output?
3. **Tool and surface:** Which AI tool, app, CLI, IDE, or agent runner should operate it? May its installed version and configuration be inspected locally?
4. **Autonomy and proof:** Which routine actions should proceed automatically, which actions need approval, and what evidence makes a run successful?
5. **Taste:** Should the loop favor speed or depth, small or cohesive changes, narrow instructions or proactive initiative, quiet exceptions or regular updates, and single-threaded or parallel work?

Use selectable choices when available, but always offer free text. Provide a recommended default in each choice set. Do not ask the user to name technical controls they may not know; translate their intent into controls later.

## Inspectable facts

Discover these instead of asking when access exists:

- repository instructions, branch and worktree state, build/test/lint commands, and protected areas;
- installed AI tool/version, model configuration, sandbox, permission mode, plugins, MCPs, hooks, and available schedulers;
- existing issue/queue, CI, state, log, notification, and approval surfaces;
- current official documentation and release notes;
- organizational policies already defining secrets, production, deployment, data, or review rules.
- product inventory, current owners, release calendars, business metrics, shared services, and cross-product dependencies when these are available.

Use only read-only probes during discovery. Do not upgrade a tool, change permissions, log in, expose secrets, or enable an integration to answer the interview.

## Conditional follow-up

Ask only the unanswered questions that affect the recommendation:

- What cadence and volume should the loop handle?
- What business model, customer promise, revenue driver, regulatory constraint, or service-level commitment changes prioritization?
- For multiple products, how should scarce capacity be shared and which product or deadline may preempt others?
- For an organization, where do policy, budget, product, and functional authority sit?
- For a solopreneur, how much owner attention is available and when should the loop stay silent?
- Where should concise state and run evidence persist?
- What time, token, API-credit, or financial budget applies?
- What constitutes no progress, and how many retries are acceptable?
- Who receives an approval request, and how quickly must they respond?
- What should happen when approval times out?
- Which data, systems, paths, branches, people, or actions are prohibited?
- Does the user want drafts only, local changes, PRs, deployments, messages, or full end-state completion?

## Taste profile

Record the user’s preference on these dimensions. Infer and state defaults when no answer is necessary.

| Dimension | Useful range |
| --- | --- |
| Initiative | exact instructions → bounded proactivity → broad ownership |
| Change size | one-line/micro → small increments → cohesive feature slices |
| Quality posture | fastest passing result → balanced → exhaustive proof |
| Communication | every step → milestones → blockers and decisions only |
| Cadence | manual → event-driven → scheduled → continuously available |
| Parallelism | one worker → bounded fan-out → independent competing attempts |
| Cost posture | hard minimum → bounded value → quality-first within a cap |
| State style | ephemeral → concise ledger → durable, reviewable project memory |
| Business focus | growth → reliability → margin → customer success → compliance |

For a 90–95% autonomous preference, default communication to milestones plus blockers, make routine reversible work automatic, and concentrate human interaction into approval packets for critical decisions.

## Approval packet

When a gate is reached, present one concise packet:

- proposed action and why it is needed;
- exact target and blast radius;
- evidence and verification status;
- expected external effect;
- rollback or recovery path;
- alternatives, including doing nothing;
- the precise approval requested.

Do not continue past the gate until the approval is explicit. Preserve state so the loop can resume without repeating completed work.

## Interview handoff

Before recommending, summarize:

- known setup and verified version;
- business model, operating topology, products/functions, value flow, and ownership;
- desired outcome and operating cadence;
- dynamic cadence, model/reasoning, and token-budget preferences;
- taste profile;
- automatic, approval-required, and prohibited actions;
- success evidence and budgets;
- assumptions and only the material unresolved choice.

Correct misunderstandings before implementing a loop, but do not require a ceremonial confirmation when the user’s intent is already clear and the next action is reversible.
