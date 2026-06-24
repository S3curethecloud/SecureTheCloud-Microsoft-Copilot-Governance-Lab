# Platform Readiness Architecture

**Phase:** 2 — Platform Readiness Architecture / Evidence Workspace Shell  
**Status:** Implementation In Progress  
**Boundary:** Enterprise-grade platform foundation, not a live production platform.

## Purpose

This document defines the next scaling layer for the SecureTheCloud Microsoft Copilot Governance Lab. Phase 2 introduces platform architecture structure without introducing live services, backend APIs, tenant connections, authorization behavior, token issuance, runtime sessions, production enforcement, or real customer data handling.

## Target posture

The repository is moving from an enterprise-grade lab toward an enterprise-grade platform foundation. Phase 2 adds the shape of a platform while preserving simulation-only execution.

## Platform layers

| Layer | Phase 2 state | Future platform state |
|---|---|---|
| Evidence input | Synthetic fixtures | Optional governed read-only evidence connectors in a future phase |
| Evaluation | Local deterministic evaluator | Job-based evaluation service in a future phase |
| Workspace | Static Markdown and JSON shell | Interactive evidence workspace in a future phase |
| Identity | None | Login and RBAC only after explicit governed authorization phase |
| Persistence | Local generated artifacts | Versioned workspace/run storage in a future phase |
| Backend API | None | Read-only API only after explicit governed backend phase |
| Enforcement | None | Not authorized in Phase 2 |

## Phase 2 workspace shell

The workspace shell consists of:

- `workspace_index.json`
- `evidence_workspace.md`
- control group navigation
- priority failed findings
- artifact inventory
- claims boundary text

These outputs are generated from synthetic evaluator output only.

## Non-goals

Phase 2 does not implement:

- Microsoft Graph integration
- Microsoft Purview API integration
- SharePoint or OneDrive scans
- live evidence collection
- OAuth or token storage
- login or RBAC
- tenant model
- backend API
- database persistence
- production enforcement
- SOC 2 certification or operating-effectiveness claims

## Enterprise-grade design principles

- deterministic evidence generation
- schema-backed output contracts
- CI-verifiable behavior
- claims-safe wording
- clear phase gates
- no runtime authority by default
- no live tenant mutation
- local-first reproducibility

## Readiness gate

Phase 2 can close only when:

- workspace shell code is committed
- workspace index schema exists
- sample workspace artifacts are committed
- tests validate workspace generation
- GitHub Actions CI passes
- phase evidence is recorded
