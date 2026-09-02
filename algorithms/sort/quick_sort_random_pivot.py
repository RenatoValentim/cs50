import random


def partition(vals, low, hight):
    random_idx = random.randint(low, hight)
    aux = vals[random_idx]
    vals[random_idx] = vals[hight]
    vals[hight] = aux
    pivot = vals[hight]
    i = low - 1
    for j in range(low, hight):
        if vals[j] < pivot:
            i += 1
            aux = vals[i]
            vals[i] = vals[j]
            vals[j] = aux
    aux = vals[i+1]
    vals[i+1] = pivot
    vals[hight] = aux
    return i+1


def quick_sort_random_pivot(vals, low=0, hight=None):
    if len(vals) == 0 or len(vals) == 1:
        return vals
    if hight is None:
        hight = len(vals)-1
    if low < hight:
        pivot = partition(vals, low, hight)
        quick_sort_random_pivot(vals, low, pivot-1)
        quick_sort_random_pivot(vals, pivot+1, hight)
    return vals
