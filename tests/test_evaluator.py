from stc_copilot_lab.evaluator import evaluate_lab_state, load_state


def test_fixture_evaluation_is_deterministic():
    state = load_state("data/fixtures")
    first = evaluate_lab_state(state)
    second = evaluate_lab_state(state)
    assert first["evidence_manifest"]["sha256"] == second["evidence_manifest"]["sha256"]


def test_phase_zero_fixture_keeps_adoption_not_ready_until_critical_gaps_are_fixed():
    state = load_state("data/fixtures")
    result = evaluate_lab_state(state)
    assert result["mode"] == "simulation"
    assert result["authority"] == "no_runtime_authority"
    assert result["adoption_status"] == "not_ready"

    controls = {item["control_id"]: item for item in result["control_results"]}
    assert controls["COPILOT-CA-001"]["status"] == "pass"
    assert controls["COPILOT-CA-002"]["status"] == "fail"
    assert controls["COPILOT-DLP-003"]["status"] == "fail"
    assert controls["COPILOT-SP-001"]["status"] == "fail"
    assert controls["COPILOT-ADOPT-001"]["status"] == "fail"


def test_clean_fixture_can_be_ready():
    state = load_state("data/fixtures")
    state = dict(state)
    state["users"] = [u for u in state["users"] if u["user_type"] != "guest"]
    state["conditional_access_policies"] = state["conditional_access_policies"] + [
        {
            "id": "ca-002",
            "name": "Require compliant device for Copilot Pilot",
            "enabled": True,
            "target_groups": ["M365-Copilot-Pilot"],
            "actions": ["require_compliant_device"],
        }
    ]
    state["dlp_policies"] = state["dlp_policies"] + [
        {
            "id": "dlp-002",
            "name": "Exclude labeled sensitive content",
            "enabled": True,
            "actions": ["exclude_labeled_sensitive_items"],
        }
    ]
    state["files"] = [
        {**f, "sharing": ["finance-team"]} if f["id"] == "file-002" else f
        for f in state["files"]
    ]
    state["connectors"] = [
        {**c, "scopes": ["read:records"], "revocation_plan": "Remove enterprise app assignment."}
        if c["name"] == "Custom CRM" else c
        for c in state["connectors"]
    ]

    result = evaluate_lab_state(state)
    assert result["adoption_status"] == "ready"
    assert all(item["status"] == "pass" for item in result["control_results"])
