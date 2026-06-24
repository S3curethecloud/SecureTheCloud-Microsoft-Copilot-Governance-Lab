"""JSON Schema validation helpers for lab fixtures and evidence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft7Validator


REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = REPO_ROOT / "schemas"


class SchemaValidationError(ValueError):
    """Raised when lab input or generated evidence fails schema validation."""


def _load_schema(name: str) -> dict[str, Any]:
    path = SCHEMA_DIR / name
    return json.loads(path.read_text(encoding="utf-8"))


def validate_with_schema(instance: Any, schema_name: str) -> None:
    schema = _load_schema(schema_name)
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        formatted = "; ".join(
            f"{'.'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
            for error in errors
        )
        raise SchemaValidationError(f"Schema validation failed for {schema_name}: {formatted}")


def validate_lab_state(state: dict[str, Any]) -> None:
    validate_with_schema(state, "lab_state.schema.json")


def validate_control_results(results: list[dict[str, Any]]) -> None:
    validate_with_schema(results, "control_results.schema.json")


def validate_evidence_manifest(manifest: dict[str, Any]) -> None:
    validate_with_schema(manifest, "evidence_manifest.schema.json")
