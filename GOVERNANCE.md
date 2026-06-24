# Governance

## Purpose

This repository provides a Microsoft Copilot governance lab for SecureTheCloud readiness, evidence, and risk-analysis workflows.

It is not a canonical doctrine source. Canonical doctrine remains in `S3curethecloud/securethecloud-doctrine-control-plane`.

## Authority model

The lab may:

- evaluate synthetic Microsoft 365 Copilot governance evidence
- score simulated readiness controls
- package synthetic evidence into local artifacts
- document secure adoption gates
- model connector approval and prompt/data leakage scenarios

The lab may not:

- mutate Microsoft 365, Entra, Purview, SharePoint, OneDrive, or Copilot configuration
- grant access or authorization
- issue tokens
- create runtime sessions
- claim production enforcement
- claim SOC 2 certification
- bypass SENTINEL for any runtime-impacting control decision

## Change management

Material changes should be phase-gated in `docs/phases/PHASE_TRACKER.md` and must preserve claims-safe boundaries.

Material changes include:

- adding live Microsoft collectors
- changing control IDs or severity semantics
- changing evidence package claims
- introducing new data sources
- adding connector behavior
- changing customer-facing wording
- changing compliance claims

## Evidence posture

Phase 0 evidence is synthetic design/readiness evidence only. It does not prove Microsoft tenant control operation, SOC 2 operating effectiveness, or independent audit attestation.
