import pytest
from random import randint

from .testtools import TestTools
from ..tools.get_pid import get_errors


@pytest.mark.parametrize("arr, expected", TestTools.get_random_values())
def test_get_errors_1(arr, expected):
    """
    Cheching if input values are equal to the expected ones
    """
    assert get_errors(arr) == expected

@pytest.mark.parametrize("arr", TestTools.get_wrong_values())
def test_get_errors_2(arr):
    """
    Checking if function reacts on wrong values
    """
    get_errors(arr) == -1
