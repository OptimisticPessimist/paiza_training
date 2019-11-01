import pytest
from src.c070 import *

@pytest.mark.parametrize("card, expected", [
    ("7777", "Four Card"),
    ("2229", "Three Card"),
    ("5566", "Two Pair"),
    ("2669", "One Pair"), 
    ("1689", "No Pair"),   
])
def test_judge_hands(card, expected):
    actual = judge_hands(card)
    assert actual == expected
