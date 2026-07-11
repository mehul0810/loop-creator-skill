# Business and operating topologies

Design the loop hierarchy around how the business creates value and makes decisions. Use these patterns as starting points, then adapt to the actual products, roles, customer impact, and constraints.

## Profile the business

Capture only facts that change loop design:

- business type: SaaS, plugin/app, marketplace, ecommerce, agency/service, content/media, open source, internal platform, regulated operation, or a hybrid;
- value and revenue flow: acquisition, activation, retention, transaction, delivery, subscription, sponsorship, or internal efficiency;
- operating scale: solopreneur, one product/team, multi-product portfolio, department, or organization;
- customer promise: availability, response time, quality, privacy, compliance, release cadence, or delivery deadline;
- scarce constraints: owner attention, engineering capacity, cash, API credits, support load, data access, review capacity, or shared infrastructure;
- authority: who owns priority, budget, product decisions, technical standards, customer communication, release, and production.

Do not infer priorities from generic business labels alone. A bootstrapped SaaS optimizing runway needs a different loop than a regulated SaaS optimizing evidence and approval, even when the product surface looks similar.

## Solopreneur

Use one owner console with a compact exception queue. Put lightweight workstream loops beneath it for product, customer/support, growth/content, finance/admin, and operations only when those streams produce recurring work.

- Optimize for owner attention and context switching, not simulated headcount.
- Let routine research, drafting, implementation, testing, and monitoring run quietly.
- Batch low-urgency decisions into one review window; interrupt only for deadlines, customer harm, security, spend, legal exposure, release, or irreversible action.
- Route work by leverage and business impact, with hard daily/weekly token and cash budgets.
- Avoid multiple agents discussing with each other when one bounded worker and a verifier can finish the item.

## One product

Use one product control loop holding goals, backlog, release state, customer signals, risks, and decisions. Create specialist execution loops only for recurring domains such as engineering, support, growth, analytics, security, or release proof.

- Keep one product source of truth and one prioritized queue.
- Route one bounded item to the relevant specialist, then return evidence and next action to the product loop.
- Increase cadence near incidents, launches, and release gates; reduce it when the product is stable.
- Optimize model choice per task instead of assigning the strongest model to the entire product.

## Multiple products or a portfolio

Keep each product loop autonomous within its scope. Add a thin portfolio loop that decides sequencing and shared constraints rather than implementing product work.

- Track product health, business value, deadlines, owner, WIP, release windows, shared dependencies, and unresolved decisions.
- Enforce portfolio WIP and capacity budgets so one noisy product does not consume every agent or token.
- Detect release collisions, shared-library changes, duplicate work, and cross-product risk.
- Route tasks to a product loop with a compact handoff; never preload every product’s context into every run.
- Escalate only true portfolio tradeoffs: priority conflicts, shared-service changes, budget movement, ownership gaps, or coordinated release decisions.

## Organization

Use a layered hierarchy with explicit contracts:

1. **Governance loop:** policy, risk tiers, budgets, permissions, audit, and exception rules.
2. **Portfolio/product loops:** outcomes, priorities, dependencies, release/customer risk, and capacity.
3. **Functional/service loops:** engineering platform, support, sales, finance, people, security, data, or operations services.
4. **Execution loops:** one bounded item, verifier, evidence, and terminal state.

Keep policy and approval authority above execution. Let product loops own outcomes while shared functions publish service contracts. Avoid a central orchestrator that polls every detail; it should receive compact health, exceptions, and decisions.

## Business-model adaptations

| Business | Emphasize | Typical gates |
| --- | --- | --- |
| Subscription/SaaS | retention, reliability, release quality, support signals | production, pricing, customer data, billing |
| Marketplace/ecommerce | transactions, inventory/supply, fraud, fulfillment | refunds, payouts, pricing, customer communication |
| Agency/service | client scope, deadlines, utilization, proof and handoff | client-facing send, scope/cost change, deployment |
| Content/media | research freshness, editorial calendar, distribution | publishing, attribution, legal/brand claims |
| Open source | issue/PR flow, maintainership, release artifacts, community | merge, release/tag, security disclosure |
| Internal platform | adoption, reliability, developer experience, policy | access, shared infrastructure, breaking change |
| Regulated work | traceability, data handling, separation of duties | regulated decision, sensitive data, production, audit evidence |

## Recommend the topology

Return a compact map showing each loop’s owner, input, output, state, cadence class, model route, token budget, verifier, and escalation target. For a portfolio or organization, include shared constraints and routing rules. Remove any layer that does not make a real decision or reduce repeated work.
