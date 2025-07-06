import pytest
from .testtools import TestTools
from ..tools.get_pid import get_pid

@pytest.mark.parametrize("arr, KP, KI, KD, expected", TestTools.get_pid_values())
def test_get_pid_1(arr, KP, KI, KD, expected):
    result = get_pid(arr, KP, KI, KD)
    if expected == 'list':
        assert isinstance(result, list)
    else:
        assert result == expected
