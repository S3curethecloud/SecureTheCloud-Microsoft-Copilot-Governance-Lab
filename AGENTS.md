# Agent Operating Instructions

This repository is a downstream SecureTheCloud lab repository.

Before proposing or implementing any module, evidence surface, control evaluator, customer-facing claim, connector workflow, Microsoft integration, or packaging change, agents must read the canonical doctrine control plane:

`S3curethecloud/securethecloud-doctrine-control-plane`

## Required first-read files

1. `AGENTS.md`
2. `doctrine.lock.md`
3. `docs/portfolio/AGENT_CONSUMPTION_GUIDE.md`
4. `docs/portfolio/SUITE_CATALOG.md`
5. `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
6. `docs/portfolio/STATUS_TAXONOMY.md`
7. `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
8. `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
9. `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
10. `docs/soc2/SOC2_ALIGNMENT_OVERVIEW.md`
11. `docs/soc2/SOC2_CONTROL_TRACEABILITY.md`
12. `docs/soc2/SOC2_EVIDENCE_REGISTER.md`
13. `docs/soc2/SOC2_CHANGE_MANAGEMENT.md`
14. `contracts/portfolio/*.json`

## Local posture

This lab is an unregistered downstream candidate until canonical doctrine accepts it.

Current local posture:

- lifecycle status: `planned` / `implemented_static` as phase evidence allows
- authority status: `no_runtime_authority`
- customer packaging status: not canonical customer-offerable module
- evidence status: synthetic readiness evidence only

## Non-negotiable boundaries

This repository must not claim or implement:

- live Microsoft tenant mutation
- production enforcement
- authorization grants
- token issuance
- runtime sessions
- provider mutation
- Kubernetes mutation
- SENTINEL bypass
- SOC 2 certification
- production operating effectiveness

## Data rule

Use synthetic data only unless a future phase explicitly approves live Microsoft evidence collection. Do not commit secrets, tenant IDs, production audit logs, customer content, or real user data.
