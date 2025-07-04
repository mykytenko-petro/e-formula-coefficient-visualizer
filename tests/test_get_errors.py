import pytest
from random import randint
from .testtools import TestTools
from modules.get_pid import get_errors, ValueOutOfRangeError


@pytest.mark.parametrize("arr, expected", TestTools.get_random_values_for_get_errors())
def test_get_errors_1(arr, expected):
    """
    Cheching if input values are equal to the expected ones
    """
    assert get_errors(arr) == expected

@pytest.mark.parametrize("arr", [([8000]), ([-1]), ([-1, 8000])])
def test_get_errors_2(arr):
    """
    Checking if function reacts on wrong values
    """
    with pytest.raises(ValueOutOfRangeError):
        get_errors(arr)
