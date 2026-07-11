# Verification and operations

Verification is the mechanism that can say “not yet.” It must evaluate the outcome of a run rather than trusting a completion message.

At a 90–95% autonomy target, automated verification carries most routine oversight. Human attention should concentrate on critical approval gates, semantic judgment that cannot yet be encoded, and repeated failures—not approval of every tool call.

## Build an acceptance stack

Use the cheapest reliable evidence first, then add semantic review only where it is needed.

1. **Preflight:** confirm the item is eligible, inputs are fresh, scope is correct, and authority exists.
2. **Deterministic result checks:** tests, type checks, linting, data assertions, HTTP checks, schema validation, or artifact existence.
3. **Regression checks:** verify that the change did not break existing required behavior.
4. **Semantic review:** a rubric-based reviewer or human checks relevance, safety, completeness, policy compliance, and user value.
5. **State check:** verify that the desired external state—not just a local file—has changed when that is the real goal.

Use a single explicit pass rule. For example: “Targeted tests and lint must pass, no unrelated files may change, and the reviewer rubric must contain no blocking finding.”

## Design an evaluator

A useful evaluator specifies:

- **Input:** the artifact, patch, transcript, environment state, or all of these.
- **Assertions:** measurable requirements and prohibited shortcuts.
- **Evidence:** the command, URL, query, review note, or state snapshot that proves each assertion.
- **Decision:** pass, fail with repairable feedback, no-op, block, or escalate.
- **Calibration:** periodic human review of rubric-based judgments, especially after a model or prompt change.

Keep quality and regression evaluation distinct. A capability test asks whether a new behavior works; a regression suite asks whether previously accepted behavior remains reliable. Promote successful representative cases into ongoing regression checks when useful.

## Track useful operational signals

Track only metrics that drive a decision:

| Signal | It helps answer |
| --- | --- |
| Pass / no-op / blocked / failed rate | Is the loop producing useful results? |
| Repeated failure fingerprint | Is a retry harmful or is a human decision required? |
| Time, tool calls, token/cost usage | Is the loop within its budget? |
| Age of source input | Did the loop act on stale state? |
| Rework or rollback rate | Does the stated verifier catch meaningful defects? |
| Human escalation rate and delay | Is autonomy appropriate for this work? |

Do not optimize an easily gamed metric alone. A loop that closes many tasks by weakening tests, producing shallow output, or expanding scope is not healthy.

## Diagnose non-convergence

| Symptom | Likely cause | Safe response |
| --- | --- | --- |
| Same error recurs | Missing prerequisite, wrong hypothesis, or transient dependency | Stop after the configured retry and record the fingerprint. |
| Checks pass but output is poor | Verifier measures the wrong thing | Strengthen the rubric or add an outcome/state check. |
| Scope keeps expanding | Goal or item boundary is vague | Split the item and require a new explicit decision. |
| Agent redoes completed work | State is stale, vague, or not read | Make the state concise, authoritative, and mandatory preflight context. |
| Cost or duration grows | Feedback is slow or work is too broad | Use targeted checks, reduce the unit of work, or lower the cap. |
| Repeated noisy reports | Trigger lacks materiality or deduplication | Add an idempotency key, delta threshold, and quiet no-change exit. |

## Stop-state contract

Always emit exactly one terminal status:

- `succeeded`: all acceptance criteria are evidenced.
- `no-op`: the input is valid but no action is required; record why.
- `blocked`: an external dependency, missing data, authority gap, or ambiguity prevents safe progress.
- `failed`: the loop completed allowed remediation but verification still fails.
- `escalated`: a named owner must choose among stated options before the loop may continue.

Include the next action even on success. This creates a clean handoff rather than implicit background work.

## Test the approval boundary

Before enabling high autonomy, deliberately exercise:

1. an allowed reversible action that should proceed without interruption;
2. a destructive or externally consequential action that must ask;
3. a prohibited action that must be denied rather than offered for approval;
4. a non-interactive run where `ask_user` may behave as denial;
5. the kill switch and approval timeout path.

Treat a gate that fails to stop the agent as a failed pilot even when the task result is correct.
