# Microsoft Copilot Governance Control Matrix

## Purpose

This matrix defines Phase 0 synthetic readiness controls for Microsoft Copilot governance.

The controls are simulation controls only. They do not claim live Microsoft tenant enforcement.

| Control ID | Area | Objective | Severity |
|---|---|---|---|
| COPILOT-RISK-001 | Intake | A use case has an owner, data classes, and review state. | High |
| COPILOT-ID-001 | Identity | Pilot users are scoped through a named Entra group. | High |
| COPILOT-ID-002 | Identity | Guest access is reviewed before pilot inclusion. | High |
| COPILOT-CA-001 | Conditional Access | Pilot users require MFA. | Critical |
| COPILOT-CA-002 | Conditional Access | Pilot users require a compliant device. | High |
| COPILOT-PURVIEW-001 | Purview | Required sensitivity labels exist. | High |
| COPILOT-DLP-001 | DLP | Sensitive prompt content is restricted by policy. | Critical |
| COPILOT-DLP-002 | DLP | Web grounding is restricted for sensitive prompt content. | High |
| COPILOT-DLP-003 | DLP | Highly sensitive labeled items are excluded from Copilot processing. | Critical |
| COPILOT-SP-001 | SharePoint and OneDrive | Sensitive content is not broadly shared. | Critical |
| COPILOT-PROMPT-001 | Scenario testing | Prompt and data exposure scenarios have expected outcomes. | High |
| COPILOT-CONN-001 | Connectors | Connectors require owner, scopes, review state, and revocation plan. | High |
| COPILOT-AUDIT-001 | Audit | Required Copilot and governance events are present. | High |
| COPILOT-ADOPT-001 | Adoption | Readiness remains gated when critical controls fail. | Critical |

## Scoring

- `pass`: objective is satisfied in the fixture set.
- `fail`: objective is not satisfied.
- `warn`: objective is partially satisfied or needs owner review.

## Adoption rule

Secure adoption can be marked `ready` only when all Critical controls pass and no High control is unresolved without an accepted risk record.
