# Approval and cadence recipes

Choose mechanisms supported by the actual tool and surface. An approval gate is complete only when it can deliver a request, persist a pause, authenticate a decision, and resume idempotently. Adaptive cadence is complete only when a real event, scheduler, or verified rescheduling API implements it.

## Approval state machine

Use `not_required`, `pending`, `approved`, `denied`, `expired`, or `cancelled`.

1. Persist the proposed action and evidence before notifying.
2. Set `pending`, a stable request identifier, owner, destination, and expiry.
3. Exit `escalated` without performing the gated action.
4. On wake-up, re-fetch the decision from the authoritative surface and verify the actor.
5. Re-check freshness, target, diff, cost, and blast radius; stale approval never transfers silently to a changed action.
6. Execute exactly once using the item and approval identifiers as idempotency keys.
7. Record the result or preserve unchanged state on denial/expiry.

## Approval adapters

| Surface | Deliver and pause | Authenticate and resume |
| --- | --- | --- |
| GitHub issue | Create/update one issue with `approval:pending`; store request ID and proposed target; exit. | Require a named owner/team decision or label plus a structured comment; re-fetch before a new workflow dispatch. |
| Pull request | Keep the consequential step in a protected environment/job or separate workflow; attach evidence to the PR. | Use required review/environment approval; resume from the protected event and revalidate the commit SHA. |
| Slack/Teams/chat | Send one packet with stable request ID; do not keep a process waiting. | Accept only an authenticated response from the named owner through a verified integration; a scheduled/event wake-up re-fetches it. |
| File or repository queue | Write an atomic request file or tracked record; exit. | A separate authorized actor writes a decision containing request ID, actor, decision, and time; never treat editing the proposal itself as approval. |
| Database/task system | Insert a pending decision row with immutable proposal hash. | Resume on a decision event or probe; verify owner identity, status transition, and unchanged proposal hash. |
| Interactive agent only | Present the packet and stop before the action. | Resume in the same durable task if supported; otherwise start a fresh run from state and revalidate approval. |

Do not recommend email replies, reaction emoji, labels, or free-form comments as approval unless the integration can authenticate the actor and map the response unambiguously.

## Cadence adapters

### Event-first

Use a webhook, queue event, CI event, task update, or repository event. Deduplicate by stable source ID, re-fetch current state, and ignore obsolete events. This is the preferred form of dynamic cadence.

### Static wake-up with cheap probe

Use cron, a fixed GitHub Actions schedule, or a platform automation only as a wake-up ceiling. Run a read-only probe first:

```text
load compact state -> check kill switch/budget/approval -> fetch minimal signal
if not eligible: update next reason and exit no-op
if eligible: dispatch the routed work run
```

Use no-change streaks, deadlines, and budget to decide whether the expensive run is eligible. The static scheduler may wake frequently while most probes exit cheaply; it is the eligibility policy—not cron itself—that adapts.

### Verified self-rescheduling

Use only when the platform exposes a documented API for changing the next run. Cap the minimum/maximum interval, preserve one active schedule, record the old and new wake-up, and require approval before creating a materially more frequent or expensive recurrence.

### Manual continuation

When no reliable scheduler exists, write the next eligible time/condition into state and return a concise command or owner action. Do not imply unattended operation.

## Failure and timeout rules

- Treat notification failure as `blocked`; never perform the gated action because delivery failed.
- Treat approval timeout as denial or continued pause according to the contract, never implicit approval.
- Use exponential backoff only for delivery/infrastructure failures, not for denied decisions or failed results.
- Cancel superseded requests and bind every approval to the current proposal hash or immutable target revision.
- Keep the kill switch outside the same untrusted input path that can trigger work.
