def walk_values(ll: LinkedList) -> list:
    vals = []
    for val in ll:
        vals.append(val)
    return vals


def assert_doubly_consistent(ll):
    length = len(ll)
    current = ll.get(0) if length > 0 else None
    if current is None:
        return

    assert current.prev is None, "head.prev should be None"

    seen = 0
    while current is not None and seen <= length:
        if current.next is not None:
            assert current.next.prev is current, "next.prev does not point back to the current node"
        current = current.next
        seen += 1

    assert seen == length, "walked more nodes than length — possible cycle"
