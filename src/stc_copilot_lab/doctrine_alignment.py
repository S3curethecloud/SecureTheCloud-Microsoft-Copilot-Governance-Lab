"""Downstream doctrine contract alignment for the Copilot Governance Lab."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .schema_validation import validate_with_schema


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = REPO_ROOT / "data" / "doctrine" / "contract_consumption_manifest.json"


def load_contract_consumption_manifest(path: str | Path = DEFAULT_MANIFEST) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _check(check_id: str, title: str, passed: bool, evidence: dict[str, Any]) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "title": title,
        "status": "pass" if passed else "fail",
        "evidence": evidence,
    }


def build_doctrine_alignment_report(result: dict[str, Any], manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    """Build a static downstream doctrine-alignment report from local evidence output."""

    manifest = manifest or load_contract_consumption_manifest()
    contract_paths = manifest["active_machine_readable_contracts"]
    forbidden_actions = set(manifest["forbidden_downstream_actions"])
    expected_contracts = {
        "contracts/portfolio/suite_catalog.json",
        "contracts/portfolio/module_registry.json",
        "contracts/portfolio/authority_matrix.json",
        "contracts/portfolio/composition_rules.json",
        "contracts/portfolio/status_taxonomy.json",
    }
    expected_suites = {"agent_blackbox", "compliance_evidence", "runtime_assurance", "risk_intelligence"}
    actual_suites = set(manifest.get("expected_customer_offerable_suites", []))

    checks = [
        _check(
            "DOCTRINE-CONSUME-001",
            "Canonical contract paths are referenced",
            expected_contracts.issubset(set(contract_paths)),
            {"contract_paths": contract_paths},
        ),
        _check(
            "DOCTRINE-CONSUME-002",
            "Human-readable doctrine authority is preserved",
            manifest.get("canonical_doctrine_lock") == "doctrine.lock.md"
            and "docs/portfolio/AGENT_CONSUMPTION_GUIDE.md" in manifest.get("human_authority_sources", []),
            {"human_authority_sources": manifest.get("human_authority_sources", [])},
        ),
        _check(
            "DOCTRINE-AUTH-001",
            "Downstream lab has no runtime authority",
            result.get("authority") == "no_runtime_authority"
            and manifest.get("authority_status") == "no_runtime_authority"
            and manifest.get("runtime_authority_claimed") is False,
            {"result_authority": result.get("authority"), "manifest_authority": manifest.get("authority_status")},
        ),
        _check(
            "DOCTRINE-AUTH-002",
            "No local suite membership or customer-offerable claim is made",
            manifest.get("suite_membership_claimed") is False
            and manifest.get("customer_offerable_claimed") is False
            and manifest.get("module_registration_status") == "unregistered_candidate",
            {
                "suite_membership_claimed": manifest.get("suite_membership_claimed"),
                "customer_offerable_claimed": manifest.get("customer_offerable_claimed"),
                "module_registration_status": manifest.get("module_registration_status"),
            },
        ),
        _check(
            "DOCTRINE-SUITE-001",
            "Customer-offerable suite IDs are recognized but not locally invented",
            actual_suites == expected_suites,
            {"expected_customer_offerable_suites": sorted(actual_suites)},
        ),
        _check(
            "DOCTRINE-COMPOSE-001",
            "Composition and evidence do not create authority",
            manifest.get("composition_creates_authority") is False
            and manifest.get("evidence_creates_enforcement") is False
            and manifest.get("sentinel_bypass_allowed") is False,
            {
                "composition_creates_authority": manifest.get("composition_creates_authority"),
                "evidence_creates_enforcement": manifest.get("evidence_creates_enforcement"),
                "sentinel_bypass_allowed": manifest.get("sentinel_bypass_allowed"),
            },
        ),
        _check(
            "DOCTRINE-FORBID-001",
            "Universal forbidden runtime actions remain blocked locally",
            {
                "issue_tokens",
                "grant_authorization",
                "create_runtime_sessions",
                "expose_live_backend_apis",
                "enforce_runtime_allow_deny_decisions",
                "bypass_sentinel",
            }.issubset(forbidden_actions),
            {"forbidden_downstream_actions": sorted(forbidden_actions)},
        ),
    ]

    report = {
        "alignment_report": "SecureTheCloud Copilot Governance Lab Doctrine Alignment",
        "canonical_repository": manifest["canonical_repository"],
        "consumption_mode": manifest["consumption_mode"],
        "authority_status": manifest["authority_status"],
        "module_registration_status": manifest["module_registration_status"],
        "suite_membership_claimed": manifest["suite_membership_claimed"],
        "runtime_authority_claimed": manifest["runtime_authority_claimed"],
        "contract_paths": contract_paths,
        "checks": checks,
        "claims_boundary": manifest["claims_boundary"],
    }
    validate_with_schema(report, "doctrine_alignment.schema.json")
    return report


def render_doctrine_alignment_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Doctrine Contract Alignment Summary",
        "",
        f"Canonical repository: `{report['canonical_repository']}`",
        f"Consumption mode: `{report['consumption_mode']}`",
        f"Authority status: `{report['authority_status']}`",
        f"Module registration status: `{report['module_registration_status']}`",
        f"Suite membership claimed: `{report['suite_membership_claimed']}`",
        f"Runtime authority claimed: `{report['runtime_authority_claimed']}`",
        "",
        "## Contract paths consumed",
        "",
    ]
    for contract_path in report["contract_paths"]:
        lines.append(f"- `{contract_path}`")

    lines.extend([
        "",
        "## Alignment checks",
        "",
        "| Check ID | Status | Title |",
        "|---|---|---|",
    ])
    for check in report["checks"]:
        lines.append(f"| {check['check_id']} | {check['status']} | {check['title']} |")

    lines.extend([
        "",
        "## Claims boundary",
        "",
        report["claims_boundary"],
    ])
    return "\n".join(lines) + "\n"
