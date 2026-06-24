# SecureTheCloud Microsoft Copilot Governance Lab

**Status:** Phase 0 / Repository Baseline

SecureTheCloud Microsoft Copilot Governance Lab is an engineering-grade, simulation-first governance lab for secure Microsoft Copilot adoption.

The lab evaluates Microsoft 365 Copilot readiness across identity, access, data governance, DLP, oversharing, prompt/data leakage, connector approval, audit evidence, and secure adoption gates.

## Phase 0 scope

Phase 0 establishes the repository baseline and a deterministic simulation-first control engine.

Allowed in Phase 0:

- static documentation
- synthetic fixtures
- local read-only control evaluation
- policy-as-code simulation
- evidence package generation from synthetic data
- CI tests for deterministic lab behavior

Not allowed in Phase 0:

- live Microsoft tenant mutation
- live backend exposure
- production enforcement
- authorization behavior
- token issuance
- runtime session creation
- provider mutation
- Kubernetes mutation
- real customer data collection
- SOC 2 certification claims

## Core lab modules

1. Microsoft 365 Copilot risk intake
2. Entra ID access boundary
3. Conditional Access posture
4. Purview sensitivity labels
5. DLP policy simulation
6. SharePoint / OneDrive oversharing risk
7. Copilot prompt and data leakage scenarios
8. Connector approval workflow
9. Audit log and evidence capture
10. Secure adoption checklist

## Repository doctrine

Before building or changing this repository, read the canonical SecureTheCloud doctrine control plane:

`S3curethecloud/securethecloud-doctrine-control-plane`

Required first-read files:

- `AGENTS.md`
- `doctrine.lock.md`
- `docs/portfolio/AGENT_CONSUMPTION_GUIDE.md`
- `docs/portfolio/SUITE_CATALOG.md`
- `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
- `docs/portfolio/STATUS_TAXONOMY.md`
- `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
- `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
- `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`
- `contracts/portfolio/*.json`

This repository does not create local substitute doctrine. The canonical doctrine control plane remains the source of truth.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
python -m stc_copilot_lab.cli evaluate --fixtures data/fixtures --out evidence/generated
```

## Output artifacts

The local evaluator produces:

- `control_results.json`
- `evidence_manifest.json`
- `secure_adoption_summary.md`

These outputs are synthetic readiness evidence unless a future phase explicitly approves live Microsoft evidence collection.
