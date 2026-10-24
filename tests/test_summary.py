import pytest

from openb.summary import calculate_average


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_calculate_average_with_decimals():
    assert calculate_average([10, 20, 30, 40]) == 25


def test_empty_values_raise_error():
    with pytest.raises(ValueError,match="Values cannot be empty"):
        calculate_average([])
