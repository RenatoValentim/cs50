def binary_search(val, vals, il=0, ir=None):
    if ir is None:
        ir = len(vals) - 1
    if il > ir:
        return False, -1
    middle = (il + ir) // 2
    if val == vals[middle]:
        return True, middle
    if val < vals[middle]:
        return binary_search(val, vals, il, middle - 1)
    if val > vals[middle]:
        return binary_search(val, vals, middle + 1, ir)
