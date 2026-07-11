# Tool and version research

Detect the actual environment and refresh fast-changing guidance before recommending a loop. Never assume that a feature documented for the latest release exists in the installed version.

## Read-only detection sequence

1. Identify the executable, app, extension, API, or hosted agent the user actually runs.
2. Capture its exact version with the tool’s own version command, application About panel, package metadata, or official diagnostic command.
3. Capture the model or model-routing setting, operating system, run surface, approval mode, sandbox/isolation, headless support, plugins/hooks/MCPs, and current scheduler.
4. Inspect project and user configuration only where authorized. Redact secret values; record that a credential exists, not the credential itself.
5. Do not update, reinstall, authenticate, enable telemetry, or modify policy during detection.

Common CLI probes include `<tool> --version`, `<tool> version`, `<tool> --help`, and an official doctor/diagnostic command. Examples that must still be verified against current docs include `codex --version`, `claude --version` or `claude doctor`, `gemini --version`, and `copilot --version`.

If a wrapper, IDE extension, or hosted app is the real execution surface, record its version separately from the underlying CLI or model. Model name alone does not identify harness behavior.

## Web research protocol

Browse by default for every substantial recommendation:

1. Search the exact tool name, installed version, and the capability being considered.
2. Open current official CLI/app documentation, permission and sandbox docs, automation/headless docs, and the changelog or release page.
3. Check version-specific minimums, renamed or deprecated flags, platform limitations, plan/organization restrictions, and behavior differences between interactive and non-interactive runs.
4. Compare the installed version with current stable. Recommend an upgrade only when a needed capability is absent or a relevant issue is fixed, and explain the tradeoff.
5. Search the official issue tracker for relevant unresolved defects when relying on experimental, policy, headless, or scheduler behavior.
6. Use recent independent articles or field reports to identify operational pitfalls, but label them as secondary evidence.

Use version-scoped queries such as:

- `"<tool> <exact version>" permissions approvals official`
- `site:<official-domain> <tool> headless hooks sandbox`
- `site:<official-repository> <tool> release <version>`
- `site:<official-repository>/issues <feature> non-interactive`

Date the research and cite each volatile product claim near the recommendation. Prefer direct links to the relevant official page, not a search result.

## Capabilities to verify

Check only the capabilities relevant to the user’s workflow:

- non-interactive, autopilot, background, or scheduled execution;
- fine-grained allow/ask/deny policy rather than only global bypass mode;
- sandbox, worktree, container, or remote isolation;
- continuation, checkpoint, durable thread, or resumable state;
- hooks, skills, rules, plugins, extensions, MCP, and custom commands;
- model selection, context limits, rate limits, credits, and cost controls;
- reasoning/thinking controls and whether they can be changed per task or only per session;
- structured output, logs, traces, notifications, and approval callbacks;
- subagents or parallel work and their permission inheritance;
- version-specific bugs that weaken the proposed guardrails.

Do not recommend a flag or configuration snippet solely from memory. Verify its exact spelling, location, values, and behavior for the installed version.

## Tool-specific research examples

- **Codex:** verify current official OpenAI guidance for the exact Codex surface—desktop, CLI, cloud, API, goals, or automations—because permissions and persistence differ by surface.
- **Claude Code:** verify the installed version and current CLI permission modes, allowed/disallowed tool syntax, hooks, checkpointing, plugins, and non-interactive behavior in official Claude Code docs.
- **Gemini CLI:** verify `--version`, approval modes, sandbox/worktree support, and Policy Engine behavior in the official repository; check known issues for non-interactive policy behavior.
- **GitHub Copilot CLI:** verify the installed version, autopilot availability, permission rules, maximum continuation limit, and current AI-credit implications in GitHub Docs.
- **Other tools:** use the same detection and official-source hierarchy. Do not downgrade the evidence standard because the tool is less familiar.

## Recommendation evidence block

Report:

- tool, surface, installed version, model, and relevant mode;
- research date and current documented/stable version if discoverable;
- supported capabilities used in the design;
- current supported model classes, reasoning controls, pricing/credits, and routing constraints used in the design;
- unavailable, experimental, deprecated, or version-gated capabilities;
- official sources and any secondary caveats;
- whether the recommendation works now, needs configuration, or requires an upgrade decision.

If browsing or version detection is unavailable, label the recommendation `provisional` and provide the exact facts that must be verified before implementation.
