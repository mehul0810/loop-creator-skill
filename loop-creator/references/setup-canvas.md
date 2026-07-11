# Setup canvas

Use this canvas after the discovery interview to design one loop in the user's actual environment. Inspect the environment before filling gaps with questions. The objective is a version-aware recommendation and reviewable first run, not an abstract framework.

## 1. Frame the outcome

Capture a concrete before/after state:

| Question | Good answer |
| --- | --- |
| Who benefits? | A named user, team, or system. |
| What changes? | A visible artifact or state transition. |
| What does not count? | Activity without an outcome, such as “agent reviewed files.” |
| What is the smallest representative item? | One issue, build failure, report, or request. |

If the desired outcome cannot be judged, begin with a discovery or reporting loop rather than an autonomous action loop.

## 2. Map the environment

Identify the native surfaces before adding new ones:

- **Work source:** issue tracker, CI, inbox, database, schedule, queue, or manual selection.
- **Workspace:** repository, local application, cloud service, documents, or an existing control plane.
- **Agent surface:** interactive chat, CLI, scheduled task, workflow runner, or service.
- **Tool facts:** observed version, selected model, approval mode, isolation, and current documented capabilities.
- **State surface:** an existing issue, Git-tracked note, database record, or queue item with an owner.
- **Proof surface:** test command, linter, preview, state query, rubric, reviewer, or audit log.
- **Authority:** credentials, data classification, approval rules, and actions that must remain human-only.

Prefer the project’s existing issue, CI, and state conventions. Do not create a separate queue, memory system, or automation service until an existing surface is demonstrably insufficient.

## 3. Answer the design questions

Resolve these in order. Do not move to automation while an earlier answer is unknown.

1. What single event or selection yields one eligible work item?
2. What outcome would an informed reviewer accept?
3. What source material must be refreshed every run?
4. Which actions are read-only, reversible, approval-gated, or prohibited?
5. What independent evidence verifies the outcome?
6. What concise state must survive a fresh agent or a later human reviewer?
7. What cap prevents uncontrolled retries, spend, drift, or repeated notifications?
8. Which exact condition ends the run, and who resolves each kind of escalation?
9. Which 90–95% of routine behavior should be automatic, and which consequential actions form the approval boundary?
10. Which user-taste preferences should shape initiative, communication, change size, verification depth, and parallelism?

If questions 2, 5, or 8 are missing, keep the loop in `pilot` and make it report-only.

## 4. Choose an integration depth

| Depth | Use when | Deliver |
| --- | --- | --- |
| Prompt/runbook | A person starts the work and reviews every result. | Contract plus first-run prompt. |
| Local command | The workspace has stable commands and local authority. | Contract plus a dry-run command or wrapper; do not assume a scheduler. |
| Event integration | A trustworthy event already identifies eligible work. | Contract, idempotency key, and review policy. |
| Scheduled automation | Fresh signals accrue predictably and no-op output is useful. | Contract, cadence, quiet/no-change behavior, and owner handoff. |
| Autonomous remediation | Routine changes are isolated, repeatably verified, and rollback-safe while critical actions are approval-gated. | Contract, fine-grained permission policy, deterministic checks, audit trail, approval packet, and kill switch. |

Increase one level only after the previous level has representative proof. “The agent completed a task once” is not sufficient proof of a safe autonomous loop.

## 5. Produce the loop contract

Copy `assets/LOOP.md.template` into the project’s established location and replace every bracketed field. Keep it short enough for an agent and reviewer to use during a run.

Use a stable item identifier and write state in a location that can be inspected later. A run note should answer: what was fresh, what changed, which checks ran, what they proved, and what happens next.

## Example: failing CI triage

- **Signal:** one newly failed CI run on a named branch.
- **Action:** inspect logs; determine whether the failure is reproducible; create a local corrective patch only if the contract permits it.
- **Verifier:** the targeted test plus the failing job’s required command.
- **State:** issue or run note with the CI URL, failure fingerprint, commands, outcome, and owner.
- **Exit:** success when checks pass; no-op for a flaky or superseded run; blocked when credentials or a third-party service is needed; escalation for changes outside the permitted package.

This is safer and more useful than “watch CI and fix anything.”
