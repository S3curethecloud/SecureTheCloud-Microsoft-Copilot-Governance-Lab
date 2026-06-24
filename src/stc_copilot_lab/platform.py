"""Static governance platform control plane shell generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schema_validation import validate_with_schema


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTRY = REPO_ROOT / "data" / "platform" / "workspace_registry.json"
PLATFORM_BOUNDARY = (
    "Static simulation control plane shell only. No live Microsoft tenant connection, authentication, "
    "authorization, RBAC, token issuance, runtime sessions, backend API exposure, database persistence, "
    "production enforcement, real customer data, SOC 2 certification claim, or production operating-effectiveness claim."
)


def load_workspace_registry(path: str | Path = DEFAULT_REGISTRY) -> dict[str, Any]:
    registry = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_with_schema(registry, "platform/workspace_registry.schema.json")
    return registry


def build_platform_registry(registry: dict[str, Any] | None = None) -> dict[str, Any]:
    registry = registry or load_workspace_registry()
    validate_with_schema(registry, "platform/workspace_registry.schema.json")
    return registry


def build_governance_command_center(result: dict[str, Any], registry: dict[str, Any] | None = None) -> dict[str, Any]:
    registry = registry or load_workspace_registry()
    failed = result["summary_counts"]["by_status"].get("fail", 0)
    passed = result["summary_counts"]["by_status"].get("pass", 0)
    return {
        "workspace_id": "command_center",
        "title": "Governance Command Center",
        "platform_status": "simulation_ready",
        "platform_mode": registry["platform_mode"],
        "authority": registry["authority"],
        "workspace_count": len(registry["workspaces"]),
        "evidence_status": "synthetic_evidence_available",
        "assessment_status": result["adoption_status"],
        "doctrine_alignment_status": "downstream_reference_only",
        "control_summary": {
            "passed": passed,
            "failed": failed,
            "total": passed + failed + result["summary_counts"]["by_status"].get("warn", 0),
        },
        "workspaces": [w["workspace_id"] for w in registry["workspaces"]],
        "claims_boundary": PLATFORM_BOUNDARY,
    }


def build_executive_dashboard(result: dict[str, Any], registry: dict[str, Any] | None = None) -> dict[str, Any]:
    registry = registry or load_workspace_registry()
    by_status = result["summary_counts"]["by_status"]
    passed = by_status.get("pass", 0)
    failed = by_status.get("fail", 0)
    total = passed + failed + by_status.get("warn", 0)
    coverage = round((passed / total) * 100, 2) if total else 0.0
    return {
        "workspace_id": "executive_dashboard",
        "title": "Executive Dashboard Workspace",
        "metrics": {
            "control_coverage_percent": coverage,
            "risk_posture": "needs_review" if failed else "ready",
            "assessment_readiness": result["adoption_status"],
            "evidence_completeness": "sample_evidence_available",
            "governance_status": "phase_4_platform_shell",
            "workspace_count": len(registry["workspaces"]),
        },
        "synthetic_only": True,
        "runtime_authority": False,
        "claims_boundary": PLATFORM_BOUNDARY,
    }


def build_assessment_history(result: dict[str, Any]) -> dict[str, Any]:
    by_status = result["summary_counts"]["by_status"]
    return {
        "workspace_id": "assessment_history",
        "assessments": [
            {
                "assessment_id": "synthetic-assessment-001",
                "date": "2026-06-24",
                "status": result["adoption_status"],
                "controls_passed": by_status.get("pass", 0),
                "controls_failed": by_status.get("fail", 0),
            }
        ],
        "synthetic_only": True,
        "runtime_authority": False,
        "claims_boundary": PLATFORM_BOUNDARY,
    }
