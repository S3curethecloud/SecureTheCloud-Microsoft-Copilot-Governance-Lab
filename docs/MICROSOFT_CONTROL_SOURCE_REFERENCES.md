# Microsoft Control Source References

**Last reviewed:** 2026-06-23  
**Scope:** Phase 1 evidence-engine control-source references for the simulation-first Microsoft Copilot Governance Lab.

## Purpose

This document records the Microsoft documentation sources used to ground the lab's synthetic control model.

The lab uses these sources for readiness modeling only. Phase 1 does not connect to Microsoft 365, Entra, Purview, SharePoint, OneDrive, or Copilot services.

## Source references

| Control area | Microsoft source | Lab mapping |
|---|---|---|
| Copilot data protection and audit architecture | https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture-data-protection-auditing | Sensitivity labels, SharePoint/OneDrive access, and audit evidence controls. |
| Purview DLP for Microsoft 365 Copilot and Copilot Chat | https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about | Prompt processing restriction, sensitive prompt web grounding restriction, and labeled content exclusion controls. |
| Purview audit logs for Copilot and AI applications | https://learn.microsoft.com/en-us/purview/audit-copilot | Copilot interaction, accessed resource, sensitivity label, policy detail, and audit evidence controls. |
| SharePoint Advanced Management readiness for Copilot and agents | https://learn.microsoft.com/en-us/sharepoint/get-ready-copilot-sharepoint-advanced-management | Oversharing, ownerless site, broad audience, and content discovery risk controls. |
| Entra Conditional Access policy templates | https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common | MFA, compliant-device, admin protection, guest access, and report-only testing posture controls. |

## Claims boundary

These references support a synthetic readiness lab. They do not prove live Microsoft tenant configuration, production control operation, independent audit testing, SOC 2 certification, or production operating effectiveness.

## Future evidence-mode expansion

A future phase may add read-only Microsoft evidence collection only if explicitly approved. Any such phase must document:

- required Microsoft permissions
- read-only API scopes
- tenant-data handling boundary
- evidence retention boundary
- no-secrets rule
- no-mutation rule
- claims-safe output wording
