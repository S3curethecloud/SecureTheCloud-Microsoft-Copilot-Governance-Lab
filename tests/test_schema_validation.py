import pytest

from stc_copilot_lab.evaluator import evaluate_lab_state, load_state
from stc_copilot_lab.schema_validation import SchemaValidationError, validate_control_results, validate_evidence_manifest, validate_lab_state


def test_lab_state_schema_accepts_fixture():
    state = load_state("data/fixtures")
    validate_lab_state(state)


def test_lab_state_schema_rejects_missing_required_section():
    state = load_state("data/fixtures")
    state.pop("risk_intake")
    with pytest.raises(SchemaValidationError):
        validate_lab_state(state)


def test_generated_evidence_matches_schemas():
    state = load_state("data/fixtures")
    result = evaluate_lab_state(state)
    validate_control_results(result["control_results"])
    validate_evidence_manifest(result["evidence_manifest"])
