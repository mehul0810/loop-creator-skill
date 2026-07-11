# Loop patterns

Choose one pattern for the first implementation. Combine patterns only after each component has a clear contract and verifier.

## Manual bounded loop

**Shape:** A human selects one item; an agent investigates or creates a limited result; checks run; a human accepts, rejects, or redirects.

**Use for:** new workflows, ambiguous requirements, sensitive data, design work, or changes that need taste and ownership judgment.

**Controls:** one item, a time/iteration cap, a clear reviewer, and a run note. Use this for discovery and the first pilot; the recommended steady state may be more autonomous.

## Event-driven loop

**Shape:** A reliable event provides an eligible item, then a handler makes a bounded response and verifies the result.

**Use for:** failed CI jobs, new tagged issues, review comments, data-quality alerts, or form submissions with a stable identifier.

**Controls:** deduplicate by event/item identifier, re-fetch source state before action, ignore obsolete events, and ensure retries are idempotent. Separate retryable infrastructure failures from result failures.

**90–95% autonomy:** allow eligible events, diagnosis, reversible remediation, verification, and state updates automatically; gate scope expansion, external publication, destructive recovery, and production changes.

## Scheduled review loop

**Shape:** A timed run gathers fresh signals and produces an evidence-backed report or an approval request.

**Use for:** backlog hygiene, recurring analysis, release readiness, monitoring, and daily triage.

**Controls:** define a cadence, lookback window, no-change behavior, and notification threshold. Report only material deltas; do not send a daily “nothing changed” message unless that is valuable to the owner.

**90–95% autonomy:** run collection, analysis, deduplication, and draft preparation quietly; notify only on material change, blocker, or a decision that meets the approval policy.

## Evaluator-refiner loop

**Shape:** A producer creates a result; a separate verifier grades it against acceptance criteria; the producer receives actionable feedback and retries within a cap.

**Use for:** code with tests, structured writing, extraction, classification, research summaries, and other work with a meaningful rubric or outcome check.

**Controls:** make the verifier able to reject; use deterministic checks before an LLM judge when possible; include a human calibration path for subjective quality; save failure reasons rather than just a score.

**90–95% autonomy:** allow bounded revise-and-recheck cycles; stop for approval when satisfying the rubric would require changing the rubric, crossing scope, or taking a consequential action.

Avoid self-critique as the only grader for consequential outputs. If the same model must produce and evaluate, make the rubric explicit and preserve a human review gate.

## Long-running builder / Ralph-style loop

**Shape:** A single agent repeatedly takes the next small prioritized increment, implements it, applies fast feedback, updates concise state, and stops at the contract boundary.

**Use for:** a well-specified greenfield or isolated workstream with strong local checks and a conscious operator. It is not a default for an existing, high-value codebase.

**Controls:** one increment per run, a prioritized plan, repository isolation, explicit allow/deny paths, fast targeted checks, a hard iteration/time/cost limit, reviewable state, and an owner who can intervene or revert. Prefer a clean branch or worktree; never normalize destructive recovery as an automatic action.

**90–95% autonomy:** allow search, implementation, targeted tests, fixes within the same item, plan/state updates, and draft PR preparation; gate dependency trust changes, destructive Git operations, merges, releases, deployments, security-sensitive changes, and expansion outside the agreed workstream.

Treat “run forever” as a smell. A repeat loop needs work exhaustion, no-progress, failure, and escalation exits.

## Human escalation loop

**Shape:** A bounded automation gathers evidence and presents a decision packet to a human, then resumes only after an explicit decision.

**Use for:** purchases, legal or policy decisions, production changes, security findings, customer communication, publishing, release/merge decisions, or uncertain data handling.

**Controls:** name the owner, required evidence, decision options, timeout behavior, and what state remains unchanged until approval.

## Pattern selection guide

| If the main uncertainty is… | Start with… |
| --- | --- |
| What success means | Manual bounded loop. |
| Whether inputs are current | Scheduled review or event loop with a freshness check. |
| Whether a result is correct | Evaluator-refiner with explicit checks. |
| Whether action is authorized | Human escalation loop. |
| How to move through a stable, well-tested backlog | Long-running builder with isolated increments. |

Do not substitute agent count for loop quality. A single agent with a sound signal, verifier, state, and stop rule is safer than a swarm with none of those controls.
