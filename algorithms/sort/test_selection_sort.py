import pytest

from algorithms.sort.selection_sort import selection_sort


@pytest.mark.parametrize(
    "vals, expected",
    [
        ([], []),                                  # empty
        ([1], [1]),                                # single
        ([2, 1], [1, 2]),                          # two, swap needed
        ([1, 2], [1, 2]),                          # two, already ordered
        ([1, 2, 3, 4], [1, 2, 3, 4]),              # already sorted
        ([4, 3, 2, 1], [1, 2, 3, 4]),              # reverse sorted (worst case)
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),  # unsorted
        ([2, 2, 2], [2, 2, 2]),                    # all duplicates
        ([3, 1, 3, 1], [1, 1, 3, 3]),              # some duplicates
        ([0, -1, 5, -10], [-10, -1, 0, 5]),        # negatives and zero
        (["c", "a", "b"], ["a", "b", "c"]),        # non-numeric, comparable
    ],
)
def test_selection_sort(vals, expected):
    assert selection_sort(vals) == expected
