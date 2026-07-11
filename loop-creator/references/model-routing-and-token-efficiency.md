# Model routing and token efficiency

Route each item to the least expensive current model and reasoning depth that can satisfy its verifier and risk requirements. Verify available models, reasoning controls, prices/credits, limits, and tool support for the installed AI tool before naming a model.

## Routing signals

Classify the item by:

- task type and determinism;
- ambiguity, novelty, and dependency count;
- blast radius, customer proximity, data sensitivity, and reversibility;
- context size and modality;
- strength of automated verification;
- latency or deadline;
- recent failure fingerprint and number of attempts;
- remaining per-run, product, and period budget.

## Capability classes

| Route | Typical work | Reasoning | Context strategy |
| --- | --- | --- | --- |
| Probe | status checks, filtering, deduplication, classification | minimal/low | identifiers and current delta only |
| Routine | extraction, formatting, bounded edits, known playbooks | low | item, required rules, targeted sources |
| Standard | implementation, investigation, synthesis with good checks | medium | focused context bundle plus concise state |
| Deep | architecture, ambiguous debugging, cross-product tradeoffs | high | curated evidence, alternatives, decision constraints |
| Critical | security, regulated, high-blast-radius or irreversible decision packet | highest justified plus independent review | complete relevant evidence, policy, verifier, human gate |

Model size and reasoning depth are separate decisions. A capable model with low reasoning can be efficient for broad but routine context; a smaller model with excessive retries can cost more than a stronger model used once.

## Escalation and fallback

1. Start at the route implied by risk and complexity; never start below the minimum risk tier.
2. Escalate one tier when the verifier fails for a reasoning-related cause, ambiguity grows, or cross-domain synthesis becomes necessary.
3. Do not escalate for missing access, stale input, broken infrastructure, or an invalid specification; block or repair the environment instead.
4. Limit the fallback chain and repeated attempts. After the configured maximum, preserve evidence and escalate to the owner.
5. De-escalate after the work becomes routine and regression checks show stable quality.

For a portfolio, let each product consume from its own budget and a shared reserve. Require an owner decision before one product consumes another product’s reserved capacity.

## Token-efficient context

- Load the standing contract once per run, then only the active item, relevant source slices, current diff/state, and required policy.
- Search, filter, or query before opening large files or histories.
- Use fresh bounded execution contexts with a compact handoff instead of carrying an ever-growing conversation.
- Persist durable facts, decisions, failure fingerprints, and next actions; do not persist chain-of-thought or full transcript dumps.
- Reuse deterministic artifacts, summaries with source pointers, cached retrieval, and tool outputs while they remain fresh.
- Keep prompts and outputs structured and short; request detailed explanation only when it changes a decision or becomes evidence.
- Run targeted checks during iteration and full regression checks at the defined gate.
- Avoid sending every product’s context to a central portfolio model; send normalized health and exception packets.

## Budgets and observability

Set:

- maximum input/output tokens or tool credits per attempt when observable;
- maximum attempts and model escalations per item;
- per-run time/cost cap;
- daily/weekly or release-window product budget;
- portfolio reserve for incidents and owner-approved exceptions;
- alert threshold and behavior when usage data is unavailable.

Track model/route, reasoning level, tokens or credits, latency, retries, verifier result, rework, and human escalation. Do not compare token counts across providers as if they were identical costs; use the provider’s current billing or credit model.

## Routing policy output

Write a deterministic table with task class, minimum risk tier, preferred model class, reasoning depth, context bundle, verifier, budget, escalation condition, and fallback. Include current supported model names only after version-aware research, and date the mapping so it can be refreshed when models or pricing change.
