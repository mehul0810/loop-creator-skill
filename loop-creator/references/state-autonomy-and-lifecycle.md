# State, autonomy, and lifecycle

Use one compact state envelope so a fresh agent, scheduler, or reviewer can resume without rereading a transcript. Adapt the storage surface, not the meaning of the core fields.

## Canonical state envelope

Copy `assets/loop-state.example.json` for JSON storage and validate it against `assets/loop-state.schema.json`. Keep these sections across JSON, YAML, issue fields, or database records:

- identity: schema version, loop identifier, item identifier, and update time;
- status: one terminal or active state plus the current maturity level;
- source: trigger, freshness time, idempotency key, and source pointer;
- progress: attempt, failure fingerprint, last action, evidence, decision, and next action;
- cadence: class, next time or trigger, reason, no-change streak, and remaining budget;
- routing: route, model, reasoning depth, attempts, and observable token/cost use;
- lineage: observation, learning candidate, decision, action, verification, durable artifact pointers, verification window, and measured outcome;
- approval: state, requested action, owner, delivery surface, request identifier, timeout, decision, and decision actor;
- safety: trust classification, policy version, kill-switch state, and prohibited-action hits;
- extensions: setup-specific values that do not redefine core semantics.

Write state atomically when possible. Never store secrets, chain-of-thought, full transcripts, or large source payloads. Store pointers and evidence hashes instead. Reject unknown schema versions unless a migration is defined.

Feedback and proactive loops must preserve lineage across runs. Do not treat issue creation or a passing implementation check as the final learning outcome. Record the decision/action pointer, define when the result can be evaluated, then close the loop as `met`, `missed`, `inconclusive`, or `not_applicable`. Promote a reusable lesson only after that result is reviewed; route product-specific learning to product docs and cross-product learning to the owning shared contract.

## Measure autonomy

Declare the measurement before the pilot:

```text
routine_autonomy_rate = eligible routine runs completed without unplanned human intervention
                        / all eligible routine runs
```

Use a trailing window of at least 20 eligible runs when volume permits; otherwise report the raw count and mark the rate provisional. Exclude designed approval-gated runs from the denominator and report them as `planned_gate_rate`. Count clarifications, manual repairs, permission surprises, and human rescue as unplanned interventions.

Report together:

- eligible runs and unattended completions;
- unplanned intervention rate and reasons;
- planned approval-gate count and response delay;
- pass, no-op, blocked, failed, and escalated counts;
- rollback/rework rate and verifier escapes;
- median tokens/cost and latency per successful eligible run.

Never optimize autonomy alone. A higher rate is invalid if safety gates, result quality, freshness, or classification accuracy deteriorate.

## Promote, demote, and retire

Use `pilot`, `review-only`, and `automated` maturity levels.

- Promote only after representative success, no-op, verifier-failure, approval, timeout, kill-switch, and injection tests pass and the declared observation window meets quality and intervention thresholds.
- Demote after an authority-boundary failure, verifier escape, repeated rollback, unexpected cost growth, material tool/model change, stale contract, or unresolved schema migration.
- Pause immediately after a failed approval or trust-boundary test.
- Review the contract on a fixed business cadence and after changes to models, tools, permissions, data classification, products, owners, or acceptance criteria.
- Retire when the source no longer produces useful work, expected value falls below operating cost, ownership disappears, a native automation replaces the loop, or the contract cannot be kept safe.

On retirement, disable recurrence, resolve or transfer pending approvals, preserve the final evidence and state, revoke loop-specific credentials, and record the replacement or reason.
