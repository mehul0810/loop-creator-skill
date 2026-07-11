---
name: loop-creator
description: Interview users and inspect their setup and business to design, recommend, implement, pilot, and improve version-aware, token-efficient AI work loops with roughly 90–95% autonomous execution and explicit human approval for critical or destructive actions. Use for a solopreneur, one product, multiple-product portfolio, team, or organization; for an agent loop, automation workflow, recurring process, Ralph-style coding loop, evaluator/refiner workflow, AI operating system, LOOP.md/RALPH.md control document; or when adapting cadence, model choice, reasoning depth, permissions, and budgets to a particular business, AI tool version, workflow, risk profile, and working style.
---

# Loop Creator

Turn repeated work into a current, business-aware operating system. Understand the person, business, products, organization, and environment first; then combine reliable triggers, bounded actions, independent evidence, durable state, high routine autonomy, adaptive cadence, model/reasoning routing, token budgets, and narrow approval gates.

## Interview before recommending

Inspect supplied repositories, instructions, configs, automation, validation commands, and available tool metadata before asking questions. Never make the user repeat discoverable facts.

Conduct the interview in batches of at most five short questions. Use an interactive choice UI when available, while always accepting free text. Read [references/discovery-interview.md](references/discovery-interview.md) and collect enough information to understand:

- whether the operator is a solopreneur, product team, portfolio, department, or organization, plus the business model and value flow;
- the desired outcome and one representative input/output;
- the AI tool, run surface, model, environment, and version;
- the user’s taste for initiative, change size, quality, communication, cadence, and parallelism;
- the source of work, proof of success, state location, budget, and failure behavior;
- which actions may run automatically and which require explicit approval.

Summarize the understood workflow, assumptions, and unresolved material choices. Ask a follow-up only when the answer changes architecture, authority, cost, or risk. Do not pause for preferences that can be safely inferred and stated.

## Verify the tool and current capabilities

Read [references/tool-version-research.md](references/tool-version-research.md). Detect the installed AI tool version with read-only local inspection when possible. Also record the app or CLI surface, selected model, approval/permission mode, sandbox or isolation, available hooks/plugins/MCPs, and scheduler or headless capability.

Browse the web before making a tool-specific recommendation unless the user explicitly forbids it. Search for the exact tool and installed version, current official documentation, changelog or release notes, permission controls, non-interactive behavior, persistence, budgets, and known limitations. Prefer vendor documentation and the tool’s official repository; use recent independent sources only for operational experience and label them as such.

Compare the installed version with current documentation without silently upgrading or changing configuration. Cite the evidence and date the research. If the exact version cannot be verified, say so and make the recommendation conditional rather than inventing support.

## Choose the business topology

Read [references/business-topologies.md](references/business-topologies.md). Map how value is created, which products or functions own outcomes, where shared constraints exist, and who can approve consequential actions.

- For one product, keep one product control loop with bounded specialist workstreams.
- For multiple products, separate product loops and add a thin portfolio loop for prioritization, WIP, shared dependencies, release collisions, and owner decisions.
- For an organization, separate governance, portfolio/product, and functional/service loops; keep policy and approval authority above execution.
- For a solopreneur, use one owner console and exception queue over lightweight workstream loops; minimize notifications and context switching.

Do not copy an enterprise hierarchy into a solo business or let a central portfolio loop perform every product’s work. Recommend the smallest hierarchy matching the actual business.

## Target 90–95% autonomy

Treat 90–95% as an interaction target, not a mathematically precise safety score: routine, reversible, in-scope work should continue without interruption; the remaining human attention should concentrate on consequential decisions.

Default to automatic discovery, research, planning, local edits, test execution, analysis, retry within caps, state updates, draft preparation, and other reversible work inside the agreed scope. Prefer a clean branch, worktree, sandbox, preview, or dry-run surface for autonomous mutations.

Require approval before an action that is destructive, irreversible, externally visible, security-sensitive, privacy-sensitive, expensive, or materially expands authority. Typical gates include deletion or destructive recovery, production changes, publishing or sending, merging or releasing, database migrations, customer-data access, secret or permission changes, purchases, legal commitments, and actions outside the agreed repository or system.

Use impact, reversibility, data sensitivity, customer proximity, and blast radius to classify actions. Do not ask for approval on every command; do not use a global bypass/yolo mode when finer policy controls can preserve the critical gates. Record the automatic, approval-required, and prohibited sets in the loop contract.

## Route cadence, models, and reasoning dynamically

Read [references/dynamic-cadence.md](references/dynamic-cadence.md) and [references/model-routing-and-token-efficiency.md](references/model-routing-and-token-efficiency.md).

Prefer event triggers when a trustworthy event exists. Otherwise adapt cadence to urgency, volatility, backlog age, deadline/release proximity, recent failures, owner availability, and budget. Accelerate during incidents or launches, decelerate after repeated no-change runs, pause when no eligible work exists, and record the reason for the next wake-up.

Select a current supported model class and reasoning depth per work item. Use fast/efficient models and low reasoning for deterministic triage and extraction; balanced models for bounded execution; capable models and deeper reasoning for ambiguous architecture, cross-product tradeoffs, security, or high-blast-radius decisions. Escalate after verified difficulty, not by default, and stop after the configured fallback chain.

Set per-run and period token/cost budgets. Load only the active item, relevant source slices, concise state, and required policy. Avoid loading every product or full transcript into each run. Persist decisions and evidence so later runs can resume with a compact context bundle.

## Recommend the best-fit workflow

Read [references/patterns.md](references/patterns.md), then provide one primary recommendation and at most one meaningful alternative. Explain how current tool/version capabilities and the user’s taste shaped the choice.

Structure the recommendation with [assets/recommendation.md.template](assets/recommendation.md.template):

1. business profile, operating topology, workflow, and user taste;
2. verified tool/version facts with dated sources;
3. recommended loop hierarchy and operating surfaces;
4. dynamic cadence and notification policy;
5. model/reasoning router and token/cost budget;
6. autonomy target, authority matrix, and critical approval gates;
7. verifier, state, limits, failure handling, and kill switch;
8. smallest safe pilot, rollout criteria, compatibility gaps, and alternative.

Avoid a generic list of tools. Recommend the simplest design that achieves the requested autonomy with reliable evidence and enforceable gates.

## Write the loop contract

Use [assets/LOOP.md.template](assets/LOOP.md.template) in the project’s established location. For a portfolio or organization, create one contract per independently owned loop and one compact map of routing, shared constraints, and escalation; do not create one giant prompt. Define one event or queue item and one observable outcome per run. Specify the source of truth, actor, verifier, state, cadence policy, model/reasoning route, token budget, retry policy, approval boundary, and terminal states.

Reject vague instructions such as “keep working until it is good.” Replace them with measurable acceptance criteria, a no-progress rule, and an iteration/time/cost cap. Treat the artifact or environment state—not the agent’s completion message—as the result.

## Pilot and calibrate

Run one representative pilot in isolation or preview mode before enabling recurring autonomous execution. Use [assets/first-run-prompt.md.template](assets/first-run-prompt.md.template) and write [assets/run-note.md.template](assets/run-note.md.template).

- Classify the result as `succeeded`, `no-op`, `blocked`, `failed`, or `escalated`.
- Use deterministic checks first, then a rubric-based reviewer or human for semantic quality. Read [references/verification.md](references/verification.md).
- Confirm that routine work proceeds without prompts and that each critical action actually stops for approval.
- Confirm that quiet-state cadence slows or pauses, urgent state accelerates, and model escalation occurs only on the routed conditions.
- Compare tokens/cost, latency, and result quality against a simple single-model baseline.
- Test at least one success path, one no-op, one verifier failure, and one approval-gated action before claiming the loop is ready.
- Tune the smallest failing component: trigger, context, instruction, permission, verifier, state, or stop rule. Never compensate with unlimited retries.

Do not create schedules, external writes, releases, deployments, or permission changes unless the user asks for implementation and authorizes the relevant action.

## Keep research current

Use [references/research-notes.md](references/research-notes.md) when explaining design principles. Treat stored sources as background only; refresh tool behavior and fast-changing loop-engineering recommendations during each substantial design request.
