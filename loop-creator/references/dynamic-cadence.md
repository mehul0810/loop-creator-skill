# Dynamic cadence

Choose cadence from the state of work rather than from habit. Prefer trustworthy events over polling, and use schedules only where no useful event exists or a periodic synthesis is itself valuable.

## Cadence inputs

Evaluate:

- urgency and customer/business impact;
- volatility: how quickly the source state changes;
- deadline, release, launch, incident, or service-level proximity;
- eligible backlog size, oldest-item age, and WIP;
- recent material changes, failures, blocked runs, and approval wait;
- owner availability and desired notification windows;
- model/token/cash budget remaining for the product or period;
- dependency availability and whether another run can produce new evidence.

## Cadence classes

Use explicit classes with project-specific intervals:

| Class | Use when | Behavior |
| --- | --- | --- |
| Event | A reliable event identifies new work | Run once per deduplicated eligible event. |
| Hot | Incident, imminent release/deadline, active customer harm | Short bounded interval; notify on material change or decision. |
| Active | Work is moving and another run can advance it | Moderate interval or after dependent state changes. |
| Routine | Stable recurring review or synthesis | Daily/weekly/business-specific window. |
| Cool | Repeated no-change or low-value state | Lengthen interval and suppress no-op notifications. |
| Paused | No eligible work, blocked dependency, exhausted budget, or owner pause | Do not wake until a named condition or manual resume. |

Intervals are recommendations, not universal constants. Respect platform scheduling limits, business hours, rate limits, and the user’s timezone.

## Adaptation rules

- Move hotter when impact rises, a deadline approaches, a dependency becomes available, a new eligible event arrives, or a verifier reveals active regression.
- Move cooler after repeated no-material-change runs, an empty queue, completed release, stable metrics, or a blocked dependency that cannot change before a known time.
- Pause when another run cannot produce new evidence, the budget is exhausted, the source is unavailable, the owner requests silence, or the loop has reached its terminal condition.
- Use exponential backoff with jitter for transient infrastructure errors, capped by the business deadline; do not treat result failures as infrastructure retries.
- Record `cadence_class`, `next_run_at_or_trigger`, `reason`, `no_change_streak`, and `budget_remaining` in state.

## Portfolio and organization rules

- Set a portfolio WIP cap and per-product concurrency cap.
- Reserve capacity for incidents and deadlines; do not starve maintenance indefinitely.
- Increase one product’s cadence without increasing every product’s cadence.
- Prefer a portfolio digest over many product notifications; surface only material deltas, approvals, and ownership conflicts.
- Let product loops choose execution cadence inside portfolio budget and policy.

## Token-aware cadence

Estimate whether the next run is likely to reveal new information. If not, wait for an event or lengthen the interval. Use a cheap read-only probe before starting an expensive reasoning run when the source supports it. Stop polling once expected information value is lower than the token/cash/attention cost.

## Cadence recommendation

Specify the initial class, interval or event, escalation and cooldown conditions, maximum consecutive no-change runs, quiet hours, notification threshold, and pause/resume rule. Explain which business signal justifies each transition.
