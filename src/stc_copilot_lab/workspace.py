"""Static evidence workspace shell generation for the Copilot Governance Lab."""

from __future__ import annotations

from collections import defaultdict
from typing import Any


WORKSPACE_CLAIMS_BOUNDARY = (
    "Static simulation workspace only; no live Microsoft tenant connection, no backend, "
    "no authorization behavior, no runtime sessions, no production enforcement, and no SOC 2 certification claim."
)


def _group_controls(control_results: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for control in control_results:
        parts = control["control_id"].split("-")
        group = parts[1].lower() if len(parts) >= 3 else "general"
        grouped[group].append(control)
    return dict(sorted(grouped.items()))


def build_workspace_index(result: dict[str, Any]) -> dict[str, Any]:
    """Build a static workspace index from evaluator output."""

    grouped = _group_controls(result["control_results"])
    failed = [control for control in result["control_results"] if control["status"] == "fail"]
    critical_failed = [control for control in failed if control["severity"] == "critical"]

    return {
        "workspace": "SecureTheCloud Copilot Governance Evidence Workspace",
        "workspace_mode": "static_simulation_shell",
        "platform_posture": "enterprise_ready_architecture_foundation",
        "authority": result["authority"],
        "adoption_status": result["adoption_status"],
        "summary_counts": result["summary_counts"],
        "navigation": [
            {"id": "overview", "title": "Overview", "artifact": "evidence_workspace.md#overview"},
            {"id": "controls", "title": "Control Explorer", "artifact": "evidence_workspace.md#control-explorer"},
            {"id": "findings", "title": "Failed Findings", "artifact": "evidence_workspace.md#failed-findings"},
            {"id": "artifacts", "title": "Evidence Artifacts", "artifact": "evidence_workspace.md#evidence-artifacts"},
            {"id": "boundaries", "title": "Claims Boundary", "artifact": "evidence_workspace.md#claims-boundary"},
        ],
        "control_groups": {
            group: {
                "total": len(controls),
                "failed": len([control for control in controls if control["status"] == "fail"]),
                "controls": [control["control_id"] for control in controls],
            }
            for group, controls in grouped.items()
        },
        "priority_findings": [
            {
                "control_id": control["control_id"],
                "severity": control["severity"],
                "title": control["title"],
                "recommendation": control["recommendation"],
            }
            for control in critical_failed
        ],
        "artifacts": [
            {"path": "control_results.json", "kind": "control_results", "synthetic": True},
            {"path": "evidence_manifest.json", "kind": "manifest", "synthetic": True},
            {"path": "secure_adoption_summary.md", "kind": "summary", "synthetic": True},
            {"path": "evidence_workspace.md", "kind": "workspace_snapshot", "synthetic": True},
            {"path": "workspace_index.json", "kind": "workspace_index", "synthetic": True},
        ],
        "claims_boundary": WORKSPACE_CLAIMS_BOUNDARY,
    }


def render_workspace_markdown(result: dict[str, Any], workspace_index: dict[str, Any]) -> str:
    """Render a static Markdown workspace shell."""

    lines = [
        "# Evidence Workspace Shell",
        "",
        "## Overview",
        "",
        f"Workspace: {workspace_index['workspace']}",
        f"Workspace mode: `{workspace_index['workspace_mode']}`",
        f"Platform posture: `{workspace_index['platform_posture']}`",
        f"Authority: `{workspace_index['authority']}`",
        f"Adoption status: `{workspace_index['adoption_status']}`",
        "",
        "## Navigation",
        "",
        "| Section | Artifact |",
        "|---|---|",
    ]
    for item in workspace_index["navigation"]:
        lines.append(f"| {item['title']} | `{item['artifact']}` |")

    lines.extend([
        "",
        "## Control Explorer",
        "",
        "| Group | Total controls | Failed controls | Control IDs |",
        "|---|---:|---:|---|",
    ])
    for group, meta in workspace_index["control_groups"].items():
        lines.append(f"| {group} | {meta['total']} | {meta['failed']} | {', '.join(meta['controls'])} |")

    lines.extend([
        "",
        "## Failed Findings",
        "",
        "| Control ID | Severity | Title | Recommendation |",
        "|---|---|---|---|",
    ])
    failed = [control for control in result["control_results"] if control["status"] == "fail"]
    for control in failed:
        lines.append(
            f"| {control['control_id']} | {control['severity']} | {control['title']} | {control['recommendation']} |"
        )

    lines.extend([
        "",
        "## Evidence Artifacts",
        "",
        "| Path | Kind | Synthetic |",
        "|---|---|---|",
    ])
    for artifact in workspace_index["artifacts"]:
        lines.append(f"| `{artifact['path']}` | {artifact['kind']} | {artifact['synthetic']} |")

    lines.extend([
        "",
        "## Claims Boundary",
        "",
        workspace_index["claims_boundary"],
    ])
    return "\n".join(lines) + "\n"
