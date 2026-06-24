"""Command line interface for the SecureTheCloud Copilot Governance Lab."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .evaluator import evaluate_lab_state, load_state


def _write_summary(result: dict, out_dir: Path) -> None:
    lines = [
        "# Secure Adoption Summary",
        "",
        f"Lab: {result['lab']}",
        f"Mode: {result['mode']}",
        f"Authority: {result['authority']}",
        f"Adoption status: `{result['adoption_status']}`",
        "",
        "## Control results",
        "",
        "| Control ID | Severity | Status | Title |",
        "|---|---|---|---|",
    ]
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
    print(json.dumps({"adoption_status": result["adoption_status"], "out": str(out_dir)}, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="SecureTheCloud Copilot Governance Lab")
    subparsers = parser.add_subparsers(dest="command", required=True)

    evaluate = subparsers.add_parser("evaluate", help="Evaluate synthetic fixture data")
    evaluate.add_argument("--fixtures", default="data/fixtures", help="Fixture directory containing lab_state.json")
    evaluate.add_argument("--out", default="evidence/generated", help="Output directory for generated evidence")
    evaluate.set_defaults(func=evaluate_command)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
