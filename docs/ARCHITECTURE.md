# Architecture

## Summary

The SecureTheCloud Microsoft Copilot Governance Lab is a simulation-first governance evaluator for secure Microsoft Copilot adoption.

The Phase 0 architecture is intentionally local and deterministic. It consumes synthetic fixtures, evaluates control posture, and writes synthetic evidence packages.

## Operating modes

| Mode | Status | Description |
|---|---|---|
| Simulation mode | Phase 0 active | Uses synthetic fixtures only. |
| Microsoft evidence mode | Future candidate | Read-only Microsoft Graph / Purview evidence collection, if approved. |
| Full Copilot validation mode | Future candidate | Licensed tenant validation of Copilot controls, if approved. |

## Components

| Component | Responsibility | Authority posture |
|---|---|---|
| Risk intake evaluator | Validates use-case ownership and data classification declarations. | Read-only / synthetic |
| Identity evaluator | Checks pilot group, guest, privileged, and MFA posture in fixture data. | Read-only / synthetic |
| Conditional Access evaluator | Checks fixture CA policy coverage for Copilot pilot users. | Read-only / synthetic |
| Purview label evaluator | Checks sensitivity-label taxonomy and coverage assumptions. | Read-only / synthetic |
| DLP simulator | Evaluates synthetic prompts/files against policy-as-code rules. | Simulation only |
| Oversharing detector | Flags synthetic SharePoint/OneDrive broad-access risks. | Read-only / synthetic |
| Connector workflow evaluator | Requires owner, scopes, approval state, and revocation plan. | Read-only / synthetic |
| Audit evidence evaluator | Checks synthetic audit event completeness. | Read-only / synthetic |
| Evidence builder | Packages local synthetic results into JSON and Markdown. | Evidence packaging only |

## Data flow

```text
Synthetic fixtures -> Control evaluator -> Control results -> Evidence manifest -> Secure adoption summary
```

## Boundary statement

The lab does not enforce, authorize, mutate, or configure Microsoft services. Any future live collector must be added as a separate phase and must preserve read-only scope unless canonical doctrine grants additional authority.

## Microsoft control surface alignment

The lab models readiness around current Microsoft control areas:

- Microsoft 365 Copilot data protection and audit architecture
- Purview sensitivity labels and DLP for Copilot / Copilot Chat
- SharePoint and OneDrive access and oversharing controls
- Entra Conditional Access and identity posture
- Copilot interaction audit evidence

These are modeled as synthetic controls in Phase 0.
