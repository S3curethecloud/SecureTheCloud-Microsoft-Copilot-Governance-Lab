# Secure Adoption Checklist

## Purpose

This checklist defines the Phase 0 secure adoption gate for Microsoft Copilot readiness.

## Checklist

### Identity and access

- [ ] Copilot users are scoped to a named Entra group.
- [ ] Guest users are reviewed before pilot access.
- [ ] Privileged users have explicit review records.
- [ ] MFA applies to the Copilot pilot group.
- [ ] Compliant-device requirements apply to the Copilot pilot group.

### Data governance

- [ ] Sensitivity labels include Confidential and Highly Confidential classes.
- [ ] Sensitive content has ownership metadata.
- [ ] Broad sharing is remediated or risk-accepted before rollout.
- [ ] SharePoint and OneDrive sites have owners.

### DLP and prompt governance

- [ ] DLP policy covers Copilot and Copilot Chat location.
- [ ] Sensitive information types are restricted in prompts.
- [ ] Web grounding is restricted for sensitive prompt content.
- [ ] Highly sensitive labeled items are excluded from Copilot processing.
- [ ] External or untrusted content scenarios are reviewed.

### Connector governance

- [ ] Each connector has a business owner.
- [ ] Each connector declares scopes.
- [ ] Write scopes are reviewed separately.
- [ ] Revocation plan exists.
- [ ] Expiration or recertification date exists.

### Audit and evidence

- [ ] Copilot interaction events are captured.
- [ ] DLP events are captured.
- [ ] Admin configuration changes are captured.
- [ ] Evidence package includes control results and manifest.
- [ ] Claims remain readiness-oriented unless independent proof exists.

## Adoption decision

| Decision | Meaning |
|---|---|
| `ready` | Critical controls pass and high risks are resolved or risk-accepted. |
| `review_required` | One or more high controls need owner review. |
| `not_ready` | One or more critical controls fail. |
