def partition(vals):
    pivot = vals[-1]
    left_half = []
    right_half = []
    for i in range(0, len(vals)-1):
        if vals[i] < pivot:
            left_half.append(vals[i])
        else:
            right_half.append(vals[i])
    return left_half, right_half, pivot


def naive_quick_sort(vals):
    if len(vals) == 0 or len(vals) == 1:
        return vals
    left_half, right_half, pivot = partition(vals)
    left_slice = naive_quick_sort(left_half)
    right_slice = naive_quick_sort(right_half)
    return left_slice + [pivot] + right_slice
