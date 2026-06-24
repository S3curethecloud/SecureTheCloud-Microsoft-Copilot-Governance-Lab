# Contract Consumption

**Phase:** 3 — Contract Consumption / Downstream Alignment Gate  
**Mode:** Downstream reference only

## Purpose

This document records how the Copilot Governance Lab references the canonical SecureTheCloud contract set without becoming the contract owner.

## Canonical source

Canonical source:

`S3curethecloud/securethecloud-doctrine-control-plane`

The lab references upstream contract paths and validates its downstream posture. It does not create local substitute doctrine.

## Upstream human-readable sources

- `doctrine.lock.md`
- `AGENTS.md`
- `docs/portfolio/AGENT_CONSUMPTION_GUIDE.md`
- `docs/portfolio/SUITE_CATALOG.md`
- `docs/portfolio/MODULE_AUTHORITY_MATRIX.md`
- `docs/portfolio/STATUS_TAXONOMY.md`
- `docs/portfolio/COMPOSITION_LAYER_DOCTRINE.md`
- `docs/portfolio/SENTINEL_CONTROL_POINT_RULE.md`
- `docs/portfolio/PRODUCT_PACKAGING_BOUNDARIES.md`

## Upstream JSON contract paths

- `contracts/portfolio/suite_catalog.json`
- `contracts/portfolio/module_registry.json`
- `contracts/portfolio/authority_matrix.json`
- `contracts/portfolio/composition_rules.json`
- `contracts/portfolio/status_taxonomy.json`

## Downstream posture

- module registration status: `unregistered_candidate`
- authority status: `no_runtime_authority`
- suite membership claimed: `false`
- customer-offerable claim: `false`
- runtime authority claimed: `false`
- SENTINEL bypass allowed: `false`

## Generated outputs

- `doctrine_alignment_report.json`
- `doctrine_alignment_summary.md`

Command:

```bash
python -m stc_copilot_lab.cli evaluate --fixtures data/fixtures --out evidence/generated --workspace --doctrine-alignment
```

## Boundary

Downstream reference only. Canonical doctrine remains upstream. The lab does not claim suite membership, runtime authority, production enforcement, SOC 2 certification, or production operating effectiveness.
