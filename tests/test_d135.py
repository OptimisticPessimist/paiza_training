import pytest
from src.d135 import *


@pytest.mark.parametrize("angle, expected", [
    (180, 3),
    (360, 4),
    (540, 5),
    (2160, 14)
])
def test_solution(angle, expected):
    actual = solution(angle)
    assert actual == expected


"""
コメント欄

半角スペース区切りの入力を`int`型の`list`にしたい
```
int_list = [int(x) for x in input().split()]
```
"""