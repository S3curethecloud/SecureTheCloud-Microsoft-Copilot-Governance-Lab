"""Canonical severity and status normalization for lab evidence."""

from __future__ import annotations

SEVERITIES = ("critical", "high", "medium", "low", "info")
STATUSES = ("pass", "fail", "warn")
ADOPTION_STATUSES = ("ready", "review_required", "not_ready")
SEVERITY_RANK = {"critical": 50, "high": 40, "medium": 30, "low": 20, "info": 10}


def normalize_severity(value: str) -> str:
    normalized = value.strip().lower().replace(" ", "_")
    aliases = {
        "crit": "critical",
        "sev1": "critical",
        "sev_1": "critical",
        "sev2": "high",
        "sev_2": "high",
        "warning": "medium",
        "informational": "info",
    }
    normalized = aliases.get(normalized, normalized)
    if normalized not in SEVERITIES:
        raise ValueError(f"Unknown severity: {value}")
    return normalized


def normalize_status(value: str) -> str:
    normalized = value.strip().lower().replace(" ", "_")
    aliases = {"passed": "pass", "failed": "fail", "warning": "warn"}
    normalized = aliases.get(normalized, normalized)
    if normalized not in STATUSES:
        raise ValueError(f"Unknown status: {value}")
    return normalized
