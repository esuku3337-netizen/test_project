import pytest

from conflict_lab import calculate_average


def test_conflict_lab_rounds_to_two_decimal_places():
    assert calculate_average([1, 2]) == 1.5


def test_calculate_average_rejects_empty_input():
    with pytest.raises(ValueError, match="Values cannot be empty"):
        calculate_average([])
