# Secure Adoption Summary

Lab: SecureTheCloud Microsoft Copilot Governance Lab
Mode: simulation
Authority: no_runtime_authority
Adoption status: `not_ready`

## Summary counts

| Dimension | Value | Count |
|---|---|---:|
| status | pass | 8 |
| status | fail | 6 |
| status | warn | 0 |
| severity | critical | 5 |
| severity | high | 9 |
| severity | medium | 0 |
| severity | low | 0 |
| severity | info | 0 |

## Control results

| Control ID | Severity | Status | Title |
|---|---|---|---|
| COPILOT-RISK-001 | high | pass | Risk intake completeness |
| COPILOT-ID-001 | high | pass | Copilot pilot access is group scoped |
| COPILOT-ID-002 | high | fail | Guest access reviewed before pilot inclusion |
| COPILOT-CA-001 | critical | pass | MFA applies to Copilot pilot group |
| COPILOT-CA-002 | high | fail | Compliant device applies to Copilot pilot group |
| COPILOT-PURVIEW-001 | high | pass | Required Purview sensitivity labels exist |
| COPILOT-DLP-001 | critical | pass | Sensitive prompt content is restricted |
| COPILOT-DLP-002 | high | pass | Sensitive prompt web grounding is restricted |
| COPILOT-DLP-003 | critical | fail | Labeled sensitive content is excluded from processing |
| COPILOT-SP-001 | critical | fail | Sensitive SharePoint and OneDrive content is not broadly shared |
| COPILOT-PROMPT-001 | high | pass | Prompt and data exposure scenarios define expected outcomes |
| COPILOT-CONN-001 | high | fail | Connector workflow includes owner, scopes, approval state, and revocation plan |
| COPILOT-AUDIT-001 | high | pass | Required Copilot governance audit events are present |
| COPILOT-ADOPT-001 | critical | fail | Secure adoption decision |

## Claims boundary

Readiness evidence only; no live enforcement or SOC 2 certification claim.
