from stc_copilot_lab.evaluator import evaluate_lab_state, load_state
from stc_copilot_lab.schema_validation import validate_with_schema
from stc_copilot_lab.workspace import build_workspace_index, render_workspace_markdown


def test_workspace_index_has_static_platform_boundary():
    state = load_state("data/fixtures")
    result = evaluate_lab_state(state)
    workspace = build_workspace_index(result)

    assert workspace["workspace_mode"] == "static_simulation_shell"
    assert workspace["platform_posture"] == "enterprise_ready_architecture_foundation"
    assert workspace["authority"] == "no_runtime_authority"
    assert "no live Microsoft tenant connection" in workspace["claims_boundary"]
    assert "backend" in workspace["claims_boundary"]


def test_workspace_index_schema_validation():
    state = load_state("data/fixtures")
    result = evaluate_lab_state(state)
    workspace = build_workspace_index(result)

    validate_with_schema(workspace, "workspace_index.schema.json")


def test_workspace_markdown_contains_navigation_and_findings():
    state = load_state("data/fixtures")
    result = evaluate_lab_state(state)
    workspace = build_workspace_index(result)
    markdown = render_workspace_markdown(result, workspace)

    assert "# Evidence Workspace Shell" in markdown
    assert "## Control Explorer" in markdown
    assert "## Failed Findings" in markdown
    assert "COPILOT-DLP-003" in markdown
    assert "no live Microsoft tenant connection" in markdown
