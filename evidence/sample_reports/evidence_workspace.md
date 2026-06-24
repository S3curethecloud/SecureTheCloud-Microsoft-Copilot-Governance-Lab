# Evidence Workspace Shell

## Overview

Workspace: SecureTheCloud Copilot Governance Evidence Workspace
Workspace mode: `static_simulation_shell`
Platform posture: `enterprise_ready_architecture_foundation`
Authority: `no_runtime_authority`
Adoption status: `not_ready`

## Navigation

| Section | Artifact |
|---|---|
| Overview | `evidence_workspace.md#overview` |
| Control Explorer | `evidence_workspace.md#control-explorer` |
| Failed Findings | `evidence_workspace.md#failed-findings` |
| Evidence Artifacts | `evidence_workspace.md#evidence-artifacts` |
| Claims Boundary | `evidence_workspace.md#claims-boundary` |

## Control Explorer

| Group | Total controls | Failed controls | Control IDs |
|---|---:|---:|---|
| adopt | 1 | 1 | COPILOT-ADOPT-001 |
| audit | 1 | 0 | COPILOT-AUDIT-001 |
| ca | 2 | 1 | COPILOT-CA-001, COPILOT-CA-002 |
| conn | 1 | 1 | COPILOT-CONN-001 |
| dlp | 3 | 1 | COPILOT-DLP-001, COPILOT-DLP-002, COPILOT-DLP-003 |
| id | 2 | 1 | COPILOT-ID-001, COPILOT-ID-002 |
| prompt | 1 | 0 | COPILOT-PROMPT-001 |
| purview | 1 | 0 | COPILOT-PURVIEW-001 |
| risk | 1 | 0 | COPILOT-RISK-001 |
| sp | 1 | 1 | COPILOT-SP-001 |

## Failed Findings

| Control ID | Severity | Title | Recommendation |
|---|---|---|---|
| COPILOT-ID-002 | high | Guest access reviewed before pilot inclusion | Remove guest users from the pilot or record an explicit approved exception. |
| COPILOT-CA-002 | high | Compliant device applies to Copilot pilot group | Create or enable a Conditional Access policy requiring compliant devices for Copilot pilot users. |
| COPILOT-DLP-003 | critical | Labeled sensitive content is excluded from processing | Add a DLP rule excluding Highly Confidential or equivalent labels from Copilot processing. |
| COPILOT-SP-001 | critical | Sensitive SharePoint and OneDrive content is not broadly shared | Remove broad sharing from sensitive files or record risk acceptance before adoption. |
| COPILOT-CONN-001 | high | Connector workflow includes owner, scopes, approval state, and revocation plan | Require connector owner, scopes, approval state, and revocation plan before adoption. |
| COPILOT-ADOPT-001 | critical | Secure adoption decision | Resolve failed controls or record owner-approved risk acceptance before rollout. |

## Evidence Artifacts

| Path | Kind | Synthetic |
|---|---|---|
| `control_results.json` | control_results | True |
| `evidence_manifest.json` | manifest | True |
| `secure_adoption_summary.md` | summary | True |
| `evidence_workspace.md` | workspace_snapshot | True |
| `workspace_index.json` | workspace_index | True |

## Claims Boundary

Static simulation workspace only; no live Microsoft tenant connection, no backend, no authorization behavior, no runtime sessions, no production enforcement, and no SOC 2 certification claim.
