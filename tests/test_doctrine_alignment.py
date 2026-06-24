from stc_copilot_lab.doctrine_alignment import (
    build_doctrine_alignment_report,
    load_contract_consumption_manifest,
    render_doctrine_alignment_markdown,
)
from stc_copilot_lab.evaluator import evaluate_lab_state, load_state
from stc_copilot_lab.schema_validation import validate_with_schema


def _report():
    state = load_state("data/fixtures")
    result = evaluate_lab_state(state)
    return build_doctrine_alignment_report(result)


def test_contract_consumption_manifest_preserves_downstream_boundary():
    manifest = load_contract_consumption_manifest()

    assert manifest["canonical_repository"] == "S3curethecloud/securethecloud-doctrine-control-plane"
    assert manifest["consumption_mode"] == "downstream_reference_only"
    assert manifest["local_substitute_doctrine_allowed"] is False
    assert manifest["authority_status"] == "no_runtime_authority"
    assert manifest["module_registration_status"] == "unregistered_candidate"
    assert manifest["suite_membership_claimed"] is False
    assert manifest["runtime_authority_claimed"] is False


def test_contract_alignment_report_validates_schema_and_checks_pass():
    report = _report()

    validate_with_schema(report, "doctrine_alignment.schema.json")
    assert all(check["status"] == "pass" for check in report["checks"])


def test_contract_alignment_report_blocks_runtime_authority_claims():
    report = _report()

    assert report["authority_status"] == "no_runtime_authority"
    assert report["suite_membership_claimed"] is False
    assert report["runtime_authority_claimed"] is False
    assert "no runtime authority" in report["claims_boundary"]


def test_contract_alignment_summary_contains_contract_paths():
    report = _report()
    markdown = render_doctrine_alignment_markdown(report)

    assert "# Doctrine Contract Alignment Summary" in markdown
    assert "contracts/portfolio/suite_catalog.json" in markdown
    assert "contracts/portfolio/authority_matrix.json" in markdown
    assert "DOCTRINE-FORBID-001" in markdown
