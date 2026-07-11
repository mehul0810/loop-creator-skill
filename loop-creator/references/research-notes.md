# Research-informed principles

These sources inform the methodology but do not prescribe a vendor-specific runtime. Adapt their ideas to the user’s actual tools, authority model, and project conventions.

## Core sources

1. [OpenAI, *Codex-maxxing for long-running work*](https://openai.com/index/codex-maxxing-long-running-work/), June 2026.
   - Treat a durable workstream as a place for context, decisions, and open loops; keep memory reviewable rather than letting vague history accumulate invisibly.
   - Apply it here through concise state, explicit run notes, and a distinction between repository artifacts and rolling operational context.

2. [Anthropic, *Demystifying evals for AI agents*](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026.
   - Define a task, trial, grader, transcript, outcome, harness, and evaluation suite separately. Judge results against actual environment state where possible.
   - Combine deterministic, model-based, and human grading according to risk; run multiple trials when variability matters; protect against regression as well as chasing new capability.

3. [AWS Prescriptive Guidance, *Evaluator reflect-refine loop patterns*](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/evaluator-reflect-refine-loop-patterns.html), 2026.
   - Model the loop as feedback control: generate, evaluate against criteria, correct, then stop on acceptance, escalation, or a retry cap.
   - Apply it here through explicit acceptance criteria, a verifier that can reject, bounded retries, and failure routing.

4. [Geoffrey Huntley, *Ralph Wiggum as a \"software engineer\"*](https://ghuntley.com/ralph/), July 2025.
   - Extract the useful operational lessons: keep work increments small, retain a prioritized plan and concise run knowledge, search before assuming missing implementation, and make feedback fast.
   - Do not treat the original technique’s open-ended shell-loop form or broad autonomous authority as a default. This skill adds safeguards for isolation, independent verification, permissions, and stop conditions.

5. [Loop Engineering, *What Is Loop Engineering?*](https://loopengineering.app/), accessed July 2026.
   - Use the practical framing that a loop connects discovery, handoff, verification, persistence, and scheduling, then begin with a small hypothesis-driven loop.
   - Cross-check any tool or pricing recommendation against current official documentation before use.

6. [Anthropic, *Measuring AI agent autonomy in practice*](https://www.anthropic.com/research/measuring-agent-autonomy), March 2026.
   - Experienced users combine more auto-approval with more active intervention. Effective oversight means being able to intervene when it matters, not approving every step.
   - Apply it here through high routine autonomy, observable runs, a kill switch, and narrow approval packets for consequential actions.

7. [Scale AI, *SWE Atlas is Complete: Measuring Coding Agents Across the Engineering Loop*](https://scale.com/blog/swe-atlas-complete), May 2026.
   - Distinguish occasional capability from repeatable reliability. Investigation, precise tests, complete refactors, and consistency across repeated trials remain important evaluation gaps.
   - Apply it here by testing representative success, no-op, failure, and approval paths before expanding autonomy.

8. Current official tool-control examples, accessed July 2026:
   - [Claude Code CLI reference](https://code.claude.com/docs/en/cli-usage) documents version-gated flags and allow/deny permission controls.
   - [Gemini CLI Policy Engine](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/policy-engine.md) documents allow, deny, and ask-user decisions plus approval modes.
   - [GitHub Copilot CLI autopilot](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/autopilot) documents autonomous continuation, permission behavior, and a continuation cap.
   - Treat these links as examples of why every recommendation must verify the installed version and current official behavior instead of copying a universal “autonomous” flag.

9. [OpenAI, *Automations*](https://openai.com/academy/codex-automations/) and [*Codex-maxxing for long-running work*](https://openai.com/index/codex-maxxing-long-running-work/), April–June 2026.
   - Recurring work can return to a durable context on schedules or triggers, continue until a condition is met, and adjust cadence as task state changes.
   - Apply it here through explicit cadence classes, next-wake reasons, cooldown/no-change behavior, and owner review at consequential decisions.

10. [Google Cloud Architecture Center, *Choose your agentic AI architecture components*](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components), May 2026.
   - Route models dynamically by task complexity, cost, and latency, and vary reasoning/thinking budget because deeper reasoning can improve quality while increasing latency and cost.
   - Apply it here with deterministic capability classes, per-item reasoning depth, a bounded fallback chain, and measured tokens/cost versus verifier results.

11. [Anthropic, *Building Effective AI Agents: Architecture Patterns and Implementation Frameworks*](https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns%20and%20Implementation%20Frameworks.pdf), May 2026.
   - Use simple agents for routine work, route complex cases to more capable or multi-agent workflows, and add architectural complexity only when measurement shows value.
   - Apply it here by keeping portfolio and organization control loops thin and routing bounded exceptions rather than making every task multi-agent.

12. Current primary prompt-injection guidance, accessed July 2026:
   - [OpenAI, *Understanding prompt injections*](https://openai.com/safety/prompt-injections/) explains that third-party content can inject malicious instructions and recommends layered protections, narrow access, explicit instructions, and confirmation for consequential actions.
   - [Anthropic, *Trustworthy agents in practice*](https://www.anthropic.com/research/trustworthy-agents), April 2026, explains that autonomy, harnesses, tools, permissions, and environments jointly determine risk and that no single prompt-injection defense is sufficient.
   - Apply it here by separating instruction authority from untrusted data, restricting source-to-sink paths, validating consequential destinations, testing injections, and preserving human gates.

## Design implications

- **A prompt is not a loop.** The loop also needs a trigger, state, verifier, boundaries, and exit.
- **Outcome evidence beats narrative.** A completion claim is weaker than tests, a state query, a review result, or a published artifact.
- **Feedback must be actionable.** A verifier should identify the assertion that failed so the next attempt can revise a specific cause instead of retrying blindly.
- **Memory should be compact and inspectable.** Keep durable decisions, source freshness, evidence, and next action—not a copy of the full agent transcript.
- **Autonomy is a graduated privilege.** Target high autonomy for routine reversible work, prove the gates, and reserve human attention for critical decisions and exceptions.
- **Version is part of architecture.** A loop that depends on a permission flag, hook, policy engine, or scheduler must verify that capability for the actual installed tool and surface.
- **Business topology is part of architecture.** A solo owner, one product, portfolio, and organization need different ownership, WIP, context, and escalation structures.
- **Cadence and model choice are controls.** Change them with work state, risk, and measured value instead of fixing every loop to one schedule and one premium model.
- **Token efficiency comes from routing and context discipline.** Load the active slice, persist compact state, and spend deeper reasoning only where the verifier or risk justifies it.
