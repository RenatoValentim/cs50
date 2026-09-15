import pytest
from data_structure.linked_list import LinkedList


def walk_values(ll: LinkedList) -> list:
    vals = []
    for val in ll:
        vals.append(val)
    return vals


@pytest.mark.parametrize(
    "values_to_prepend, expected_order",
    [
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
        ([5, 5, 5], [5, 5, 5]),
        ([], []),
    ],
)
def test_prepend(values_to_prepend, expected_order):
    ll = LinkedList()
    for val in values_to_prepend:
        ll.prepend(val)
    assert walk_values(ll) == expected_order


@pytest.mark.parametrize(
    "values_to_append, expected_order",
    [
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([5, 5, 5], [5, 5, 5]),
        ([], []),
    ],
)
def test_append(values_to_append, expected_order):
    ll = LinkedList()
    for val in values_to_append:
        ll.append(val)
    assert walk_values(ll) == expected_order


@pytest.mark.parametrize(
    "initial_values, val_to_find, should_find",
    [
        ([1, 2, 3], 2, True),
        ([1, 2, 3], 1, True),
        ([1, 2, 3], 3, True),
        ([1, 2, 3], 99, False),
        ([], 1, False),
    ],
)
def test_find(initial_values, val_to_find, should_find):
    ll = LinkedList()
    for val in initial_values:
        ll.append(val)

    result = ll.find(val=val_to_find)

    if should_find:
        assert result is not None
        assert result.val == val_to_find
    else:
        assert result is None


@pytest.mark.parametrize(
    "initial_values, val_to_remove, expected_return, expected_order",
    [
        ([1, 2, 3], 2, True, [1, 3]),
        ([1, 2, 3], 1, True, [2, 3]),
        ([1, 2, 3], 3, True, [1, 2]),
        ([1, 2, 3], 99, False, [1, 2, 3]),
        ([1], 1, True, []),
        ([], 1, False, []),
        (
            [1, 2, 3, 2],
            2,
            True,
            [1, 3, 2],
        ),
    ],
)
def test_remove(initial_values, val_to_remove, expected_return, expected_order):
    ll = LinkedList()
    for val in initial_values:
        ll.append(val)

    result = ll.remove(val=val_to_remove)

    assert result is expected_return
    assert walk_values(ll) == expected_order


@pytest.mark.parametrize(
    "initial_values, val_to_remove",
    [
        ([1, 2, 3], 3),
        ([1], 1),
    ],
)
def test_remove_updates_tail_correctly(initial_values, val_to_remove):
    ll = LinkedList()
    for val in initial_values:
        ll.append(val)

    ll.remove(val=val_to_remove)
    ll.append(999)
    tail = ll.get(len(ll) - 1)

    assert walk_values(ll)[-1] == 999
    assert tail is not None
    assert tail.val == 999


@pytest.mark.parametrize(
    "initial_values, expected_return",
    [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 3),
        ([5, 9], 2),
    ],
)
def test_length(initial_values, expected_return):
    ll = LinkedList()
    for val in initial_values:
        ll.append(val)

    assert len(ll) == expected_return

    if len(initial_values) == 3:
        ll.remove(2)
        assert len(ll) == 2


@pytest.mark.parametrize(
    "initial_values, index, expected_return",
    [
        ([2, 4, 8], 1, 4),
        ([2, 4, 8], -1, None),
        ([2, 4, 8], 4, None),
    ],
)
def test_get(initial_values, index, expected_return):
    ll = LinkedList()
    for val in initial_values:
        ll.append(val)

    node = ll.get(index)

    if node is not None:
        assert node.val == expected_return
    else:
        assert node == expected_return


@pytest.mark.parametrize(
    "initial_values, target_val, new_val, expected_return, expected_order",
    [
        ([2, 5, 8], 5, 7, True, [2, 5, 7, 8]),
        ([2, 5, 8], 8, 1, True, [2, 5, 8, 1]),
    ],
)
def test_inser_after(
    initial_values, target_val, new_val, expected_return, expected_order
):
    ll = LinkedList()
    for val in initial_values:
        ll.append(val)

    assert ll.insert_after(target_val, new_val) == expected_return
    assert walk_values(ll) == expected_order
    assert len(ll) == len(initial_values) + 1

@pytest.mark.parametrize(
    "values_to_append, expected_order",
    [
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
        ([5, 5, 5], [5, 5, 5]),
        ([], []),
    ],
)
def test_reverse(values_to_append, expected_order):
    ll = LinkedList()
    for val in values_to_append:
        ll.append(val)

    ll.reverse()

    assert walk_values(ll) == expected_order

    ll.append(8)

    assert ll.get(len(ll)-1).val == 8
