"""Deterministic evaluator for the SecureTheCloud Copilot Governance Lab."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


CRITICAL = "critical"
HIGH = "high"
PASS = "pass"
FAIL = "fail"
WARN = "warn"


@dataclass(frozen=True)
class ControlResult:
    control_id: str
    title: str
    severity: str
    status: str
    evidence: dict[str, Any]
    recommendation: str


def _contains_policy(policies: list[dict[str, Any]], *, action: str, target_group: str | None = None) -> bool:
    for policy in policies:
        if not policy.get("enabled", False):
            continue
        if action not in policy.get("actions", []):
            continue
        if target_group and target_group not in policy.get("target_groups", []):
            continue
        return True
    return False


def _result(control_id: str, title: str, severity: str, ok: bool, evidence: dict[str, Any], recommendation: str) -> ControlResult:
    return ControlResult(
        control_id=control_id,
        title=title,
        severity=severity,
        status=PASS if ok else FAIL,
        evidence=evidence,
        recommendation=recommendation if not ok else "No remediation required for the current fixture set.",
    )


def evaluate_lab_state(state: dict[str, Any]) -> dict[str, Any]:
    """Evaluate a synthetic lab state and return control results plus adoption status."""

    intake = state.get("risk_intake", {})
    users = state.get("users", [])
    policies = state.get("conditional_access_policies", [])
    labels = state.get("sensitivity_labels", [])
    dlp = state.get("dlp_policies", [])
    files = state.get("files", [])
    prompts = state.get("prompt_scenarios", [])
    connectors = state.get("connectors", [])
    audits = state.get("audit_events", [])

    pilot_group = intake.get("pilot_group", "M365-Copilot-Pilot")
    pilot_users = [u for u in users if pilot_group in u.get("groups", [])]
    guest_users = [u for u in pilot_users if u.get("user_type") == "guest" and not u.get("copilot_exception_approved", False)]

    required_intake = ["business_unit", "use_case", "data_classes", "risk_owner", "approval_state", "pilot_group"]
    results: list[ControlResult] = []

    results.append(_result(
        "COPILOT-RISK-001",
        "Risk intake completeness",
        HIGH,
        all(intake.get(field) for field in required_intake),
        {"required_fields": required_intake, "present_fields": sorted(k for k, v in intake.items() if v)},
        "Complete the Copilot intake record before adoption review.",
    ))

    results.append(_result(
        "COPILOT-ID-001",
        "Copilot pilot access is group scoped",
        HIGH,
        bool(pilot_users),
        {"pilot_group": pilot_group, "pilot_user_count": len(pilot_users)},
        "Assign Copilot pilot users through a named Entra group.",
    ))

    results.append(_result(
        "COPILOT-ID-002",
        "Guest access reviewed before pilot inclusion",
        HIGH,
        len(guest_users) == 0,
        {"unauthorized_guest_users": [u.get("id") for u in guest_users]},
        "Remove guest users from the pilot or record an explicit approved exception.",
    ))

    results.append(_result(
        "COPILOT-CA-001",
        "MFA applies to Copilot pilot group",
        CRITICAL,
        _contains_policy(policies, action="require_mfa", target_group=pilot_group),
        {"pilot_group": pilot_group},
        "Create or enable a Conditional Access policy requiring MFA for the Copilot pilot group.",
    ))

    results.append(_result(
        "COPILOT-CA-002",
        "Compliant device applies to Copilot pilot group",
        HIGH,
        _contains_policy(policies, action="require_compliant_device", target_group=pilot_group),
        {"pilot_group": pilot_group},
        "Create or enable a Conditional Access policy requiring compliant devices for Copilot pilot users.",
    ))

    label_names = {label.get("name", "").lower() for label in labels}
    results.append(_result(
        "COPILOT-PURVIEW-001",
        "Required Purview sensitivity labels exist",
        HIGH,
        {"confidential", "highly confidential"}.issubset(label_names),
        {"labels": sorted(label_names)},
        "Define Confidential and Highly Confidential labels before rollout.",
    ))

    results.append(_result(
        "COPILOT-DLP-001",
        "Sensitive prompt content is restricted",
        CRITICAL,
        _contains_policy(dlp, action="restrict_sensitive_prompt_processing"),
        {"configured_actions": sorted({a for p in dlp for a in p.get("actions", [])})},
        "Add a DLP rule for sensitive information types in Copilot prompts.",
    ))

    results.append(_result(
        "COPILOT-DLP-002",
        "Sensitive prompt web grounding is restricted",
        HIGH,
        _contains_policy(dlp, action="restrict_sensitive_prompt_web_grounding"),
        {"configured_actions": sorted({a for p in dlp for a in p.get("actions", [])})},
        "Add a DLP rule restricting web grounding when prompts contain sensitive content.",
    ))

    results.append(_result(
        "COPILOT-DLP-003",
        "Labeled sensitive content is excluded from processing",
        CRITICAL,
        _contains_policy(dlp, action="exclude_labeled_sensitive_items"),
        {"configured_actions": sorted({a for p in dlp for a in p.get("actions", [])})},
        "Add a DLP rule excluding Highly Confidential or equivalent labels from Copilot processing.",
    ))

    broad_scopes = {"anyone", "organization", "all_company"}
    risky_files = [
        f for f in files
        if f.get("sensitivity", "").lower() in {"confidential", "highly confidential"}
        and set(f.get("sharing", [])) & broad_scopes
    ]
    results.append(_result(
        "COPILOT-SP-001",
        "Sensitive SharePoint and OneDrive content is not broadly shared",
        CRITICAL,
        len(risky_files) == 0,
        {"risky_files": [{"id": f.get("id"), "sharing": f.get("sharing", [])} for f in risky_files]},
        "Remove broad sharing from sensitive files or record risk acceptance before adoption.",
    ))

    incomplete_prompts = [p for p in prompts if not p.get("expected_control_outcome")]
    results.append(_result(
        "COPILOT-PROMPT-001",
        "Prompt and data exposure scenarios define expected outcomes",
        HIGH,
        len(incomplete_prompts) == 0 and bool(prompts),
        {"scenario_count": len(prompts), "incomplete_scenarios": [p.get("id") for p in incomplete_prompts]},
        "Add expected control outcomes for each prompt and exposure scenario.",
    ))

    incomplete_connectors = [
        c for c in connectors
        if not all(c.get(field) for field in ["owner", "scopes", "approval_state", "revocation_plan"])
    ]
    results.append(_result(
        "COPILOT-CONN-001",
        "Connector workflow includes owner, scopes, approval state, and revocation plan",
        HIGH,
        len(incomplete_connectors) == 0,
        {"incomplete_connectors": [c.get("name") for c in incomplete_connectors]},
        "Require connector owner, scopes, approval state, and revocation plan before adoption.",
    ))

    event_types = {event.get("event_type") for event in audits}
    required_events = {"CopilotInteraction", "DlpRuleMatch", "AdminConfigChange"}
    results.append(_result(
        "COPILOT-AUDIT-001",
        "Required Copilot governance audit events are present",
        HIGH,
        required_events.issubset(event_types),
        {"required_events": sorted(required_events), "present_events": sorted(event_types)},
        "Capture Copilot interaction, DLP, and admin change events in evidence.",
    ))

    critical_failed = [r.control_id for r in results if r.severity == CRITICAL and r.status == FAIL]
    high_failed = [r.control_id for r in results if r.severity == HIGH and r.status == FAIL]
    if critical_failed:
        adoption_status = "not_ready"
    elif high_failed:
        adoption_status = "review_required"
    else:
        adoption_status = "ready"

    results.append(ControlResult(
        control_id="COPILOT-ADOPT-001",
        title="Secure adoption decision",
        severity=CRITICAL,
        status=PASS if adoption_status == "ready" else FAIL,
        evidence={"adoption_status": adoption_status, "critical_failed": critical_failed, "high_failed": high_failed},
        recommendation="Resolve failed controls or record owner-approved risk acceptance before rollout." if adoption_status != "ready" else "No remediation required for the current fixture set.",
    ))

    control_results = [asdict(r) for r in results]
    manifest_source = json.dumps(control_results, sort_keys=True).encode("utf-8")
    manifest_hash = hashlib.sha256(manifest_source).hexdigest()

    return {
        "lab": "SecureTheCloud Microsoft Copilot Governance Lab",
        "mode": "simulation",
        "authority": "no_runtime_authority",
        "adoption_status": adoption_status,
        "control_results": control_results,
        "evidence_manifest": {
            "artifact": "control_results.json",
            "sha256": manifest_hash,
            "synthetic_evidence": True,
            "claims_boundary": "Readiness evidence only; no live enforcement or SOC 2 certification claim.",
        },
    }


def load_state(fixtures_dir: str | Path) -> dict[str, Any]:
    path = Path(fixtures_dir) / "lab_state.json"
    return json.loads(path.read_text(encoding="utf-8"))
