# Threat Model

## Scope

This threat model covers Phase 0 simulation of Microsoft Copilot governance readiness. It does not cover live tenant operations.

## Assets

- Synthetic users and groups
- Synthetic Conditional Access policy records
- Synthetic SharePoint and OneDrive file metadata
- Synthetic Purview sensitivity label metadata
- Synthetic DLP policy metadata
- Synthetic connector approval records
- Synthetic Copilot audit events
- Synthetic evidence packages

## Trust boundaries

| Boundary | Description | Phase 0 posture |
|---|---|---|
| Fixture boundary | Local synthetic data used for deterministic evaluation. | Trusted test input only |
| Evaluator boundary | Local code that scores controls. | No external calls |
| Evidence boundary | Generated JSON and Markdown evidence outputs. | Synthetic readiness evidence |
| Microsoft tenant boundary | Real Microsoft 365, Entra, Purview, SharePoint, OneDrive, Copilot services. | Out of scope |

## Threat scenarios

| Scenario | Risk | Lab response |
|---|---|---|
| Overshared sensitive content | Copilot may surface content the user already has access to, including content that was accidentally shared too broadly. | Flag broad sharing on sensitive fixture files. |
| Incomplete Conditional Access | Pilot users may access Copilot without strong posture requirements. | Check MFA and compliant-device policy coverage. |
| Weak label taxonomy | Sensitive content may not be classified consistently. | Check required labels and coverage assumptions. |
| Missing DLP controls | Sensitive prompt or file content may be processed contrary to policy intent. | Evaluate fixture DLP rules and scenarios. |
| Unreviewed connector | External or custom data source may expand Copilot grounding risk. | Require owner, scopes, approval state, and revocation plan. |
| Missing audit evidence | Governance team cannot prove readiness or investigate activity. | Require Copilot interaction and governance event fixtures. |
| Claims drift | Repository may imply live enforcement or certification. | Preserve governance and claims-safe wording boundaries. |

## Non-goals

- Exploit development
- Bypass research
- Live Microsoft configuration changes
- Production incident response automation
- Real tenant data collection
- Runtime enforcement
