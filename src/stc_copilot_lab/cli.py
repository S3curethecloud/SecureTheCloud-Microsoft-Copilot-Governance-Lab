"""Command line interface for the SecureTheCloud Copilot Governance Lab."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .doctrine_alignment import build_doctrine_alignment_report, render_doctrine_alignment_markdown
from .evaluator import evaluate_lab_state, load_state
from .platform import build_assessment_history, build_executive_dashboard, build_governance_command_center, build_platform_registry
from .workspace import build_workspace_index, render_workspace_markdown


def _write_summary(result: dict, out_dir: Path) -> None:
    lines = [
        "# Secure Adoption Summary",
        "",
        f"Lab: {result['lab']}",
        f"Mode: {result['mode']}",
        f"Authority: {result['authority']}",
        f"Adoption status: `{result['adoption_status']}`",
        "",
        "## Summary counts",
        "",
        "| Dimension | Value | Count |",
        "|---|---|---:|",
    ]
    for status, count in result["summary_counts"]["by_status"].items():
        lines.append(f"| status | {status} | {count} |")
    for severity, count in result["summary_counts"]["by_severity"].items():
        lines.append(f"| severity | {severity} | {count} |")

    lines.extend([
        "",
        "## Control results",
        "",
        "| Control ID | Severity | Status | Title |",
        "|---|---|---|---|",
    ])
    for control in result["control_results"]:
        lines.append(
            f"| {control['control_id']} | {control['severity']} | {control['status']} | {control['title']} |"
        )
    lines.extend([
        "",
        "## Claims boundary",
        "",
        result["evidence_manifest"]["claims_boundary"],
    ])
    (out_dir / "secure_adoption_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_workspace(result: dict, out_dir: Path) -> None:
    workspace_index = build_workspace_index(result)
    (out_dir / "workspace_index.json").write_text(
        json.dumps(workspace_index, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out_dir / "evidence_workspace.md").write_text(
        render_workspace_markdown(result, workspace_index),
        encoding="utf-8",
    )


def _write_doctrine_alignment(result: dict, out_dir: Path) -> None:
    alignment_report = build_doctrine_alignment_report(result)
    (out_dir / "doctrine_alignment_report.json").write_text(
        json.dumps(alignment_report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out_dir / "doctrine_alignment_summary.md").write_text(
        render_doctrine_alignment_markdown(alignment_report),
        encoding="utf-8",
    )


def _write_platform(result: dict, out_dir: Path) -> None:
    platform_dir = out_dir / "platform"
    platform_dir.mkdir(parents=True, exist_ok=True)
    platform_registry = build_platform_registry()
    outputs = {
        "platform_registry.json": platform_registry,
        "governance_command_center.json": build_governance_command_center(result, platform_registry),
        "executive_dashboard.json": build_executive_dashboard(result, platform_registry),
        "assessment_history.json": build_assessment_history(result),
    }
    for filename, payload in outputs.items():
        (platform_dir / filename).write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )


def evaluate_command(args: argparse.Namespace) -> int:
    fixtures = Path(args.fixtures)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    state = load_state(fixtures)
    result = evaluate_lab_state(state)

    (out_dir / "control_results.json").write_text(
        json.dumps(result["control_results"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out_dir / "evidence_manifest.json").write_text(
        json.dumps(result["evidence_manifest"], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    _write_summary(result, out_dir)
    if args.workspace:
        _write_workspace(result, out_dir)
    if args.doctrine_alignment:
        _write_doctrine_alignment(result, out_dir)
    if args.platform:
        _write_platform(result, out_dir)
    print(json.dumps({"adoption_status": result["adoption_status"], "out": str(out_dir)}, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="SecureTheCloud Copilot Governance Lab")
    subparsers = parser.add_subparsers(dest="command", required=True)

    evaluate = subparsers.add_parser("evaluate", help="Evaluate synthetic fixture data")
    evaluate.add_argument("--fixtures", default="data/fixtures", help="Fixture directory containing lab_state.json")
    evaluate.add_argument("--out", default="evidence/generated", help="Output directory for generated evidence")
    evaluate.add_argument("--workspace", action="store_true", help="Generate static evidence workspace shell outputs")
    evaluate.add_argument("--doctrine-alignment", action="store_true", help="Generate downstream doctrine contract alignment outputs")
    evaluate.add_argument("--platform", action="store_true", help="Generate static governance platform control plane shell outputs")
    evaluate.set_defaults(func=evaluate_command)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
