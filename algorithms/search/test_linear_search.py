import pytest

from algorithms.search.linear_search import linear_search


@pytest.mark.parametrize(
    "val, vals, expected",
    [
        (1, [1, 2, 3], (True, 0)),  # first
        (3, [1, 2, 3], (True, 2)),  # last
        (2, [1, 2, 3], (True, 1)),  # middle
        (4, [1, 2, 3], (False, -1)),  # absent
        (1, [], (False, -1)),  # empty
        (1, [1], (True, 0)),  # single match
        (2, [1], (False, -1)),  # single no match
        (2, [2, 2, 2], (True, 0)),  # first duplicate wins
        (1, [9, 3, 1], (True, 2)),  # unsorted
        (0, [0, 1], (True, 0)),  # falsy value
    ],
)
def test_linear_search(val, vals, expected):
    assert linear_search(val, vals) == expected
