import pytest

from src.c049 import *


@pytest.mark.parametrize("a, b, expected", [
    (1, 3, 2),
    (17, 2, 15)
])
def test_moved_floor(a, b, expected):
    actual = moved_floor(a, b)
    assert actual == expected