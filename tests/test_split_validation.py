"""Tests for location-disjoint split validation."""

from src.datasets.split_validation import (
    validate_zero_location_overlap,
)


def test_zero_overlap():
    result = validate_zero_location_overlap(
        ["A", "B"],
        ["C", "D"],
    )

    assert result["passed"] is True
    assert result["forbidden_location_overlap"] == 0
