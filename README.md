# SecureTheCloud Microsoft Copilot Governance Lab

**Status:** Phase 4 / Governance Control Plane Shell in Progress  
**Platform Positioning:** Microsoft Copilot reference implementation for the SecureTheCloud AI Governance Platform

SecureTheCloud Microsoft Copilot Governance Lab is an engineering-grade, simulation-first governance platform foundation for secure Microsoft Copilot adoption.

This repository is the first governed domain implementation of the broader SecureTheCloud AI Governance Platform pattern. It demonstrates evidence generation, workspace architecture, doctrine alignment, platform control-plane structure, and claims-safe governance workflows for Microsoft Copilot.

The repository remains Microsoft Copilot-focused by name and scope, while the architecture is intentionally reusable for future AI governance domains such as Microsoft Security Copilot, Azure AI, AWS Bedrock, Amazon SageMaker, ServiceNow AI, and other enterprise AI platforms.

## Current platform posture

The project currently provides:

- synthetic control evaluation
- schema-backed evidence generation
- governance evidence workspaces
- downstream doctrine contract alignment
- static platform control-plane shell
- platform CLI generation path
- CI validation
- phase-gated evidence history

Authority remains:

```text
no_runtime_authority
```

Execution remains:

```text
simulation_only
```

## Boundary

This repository does **not** currently provide:

- live Microsoft tenant integration
- authentication
- authorization
- RBAC
- token issuance
- runtime sessions
- backend API exposure
- database persistence
- production enforcement
- real customer data handling
- SOC 2 certification claims
- production operating-effectiveness claims

## Core Microsoft Copilot governance modules

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

## Governance platform shell

Phase 4 introduces the platform control-plane shell:

```text
Governance Control Plane Shell
├── Governance Command Center
├── Control Catalog
├── Evidence Inventory
├── Tenant Readiness
├── Assessment History
├── Executive Dashboard
├── Doctrine Alignment
├── Evidence Engine
├── Workspace Registry
├── Platform Generator
└── Platform CLI
```

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
python -m stc_copilot_lab.cli evaluate --fixtures data/fixtures --out evidence/generated --workspace --doctrine-alignment --platform
```

## Output artifacts

The evaluator can produce:

- `control_results.json`
- `evidence_manifest.json`
- `secure_adoption_summary.md`
- `workspace_index.json`
- `evidence_workspace.md`
- `doctrine_alignment_report.json`
- `doctrine_alignment_summary.md`
- `platform/platform_registry.json`
- `platform/governance_command_center.json`
- `platform/executive_dashboard.json`
- `platform/assessment_history.json`

These outputs are synthetic readiness evidence unless a future governed phase explicitly approves live Microsoft evidence collection.

## Strategic direction

The repository should be read as:

> Microsoft Copilot is the first governed domain implemented on the SecureTheCloud AI Governance Platform pattern.

Future phases may introduce domain models, tenant and assessment abstractions, static workflow state, and additional governance domains. Runtime integrations remain out of scope unless explicitly approved by a future governed phase.
