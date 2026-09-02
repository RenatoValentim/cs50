def merge(left, right):
    il = 0
    ir = 0
    results = []
    while il < len(left) or ir < len(right):
        current_left_val = None
        current_right_val = None
        if il < len(left):
            current_left_val = left[il]
        if ir < len(right):
            current_right_val = right[ir]
        if current_right_val is None:
            results.append(current_left_val)
            il += 1
        elif current_left_val is None:
            results.append(current_right_val)
            ir += 1
        elif current_left_val is not None and current_right_val is not None:
            if current_left_val < current_right_val:
                results.append(current_left_val)
                il += 1
            elif current_right_val < current_left_val:
                results.append(current_right_val)
                ir += 1
            elif current_left_val == current_right_val:
                results.append(current_left_val)
                il += 1
                results.append(current_right_val)
                ir += 1
    return results


def merge_sort(vals):
    if len(vals) == 0 or len(vals) == 1:
        return vals
    middle = (0 + len(vals)-1) // 2
    left_half = []
    for i in range(middle+1):
        left_half.append(vals[i])
    left_slice = merge_sort(left_half)
    right_half = []
    for i in range(middle+1, len(vals)):
        right_half.append(vals[i])
    right_slice = merge_sort(right_half)
    return merge(left_slice, right_slice)
