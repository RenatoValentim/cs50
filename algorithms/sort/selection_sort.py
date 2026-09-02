def selection_sort(vals):
    for i in range(len(vals)):
        min_idx = i
        for j in range(i+1, len(vals)):
            if vals[j] < vals[min_idx]:
                min_idx = j
        temp = vals[i]
        vals[i] = vals[min_idx]
        vals[min_idx] = temp
    return vals
