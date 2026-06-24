import pytest

from stc_copilot_lab.normalization import normalize_severity, normalize_status


def test_severity_normalization_aliases():
    assert normalize_severity("Critical") == "critical"
    assert normalize_severity("sev1") == "critical"
    assert normalize_severity("Sev 2") == "high"
    assert normalize_severity("informational") == "info"


def test_status_normalization_aliases():
    assert normalize_status("Passed") == "pass"
    assert normalize_status("failed") == "fail"
    assert normalize_status("warning") == "warn"


def test_unknown_values_raise():
    with pytest.raises(ValueError):
        normalize_severity("urgent-now")
    with pytest.raises(ValueError):
        normalize_status("unknown")
