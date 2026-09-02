def bubble_sort(vals):
    for i in range(len(vals)-1):
        swapped = False
        for j in range(len(vals)-1-i):
            if vals[j] > vals[j+1]:
                temp = vals[j]
                vals[j] = vals[j+1]
                vals[j+1] = temp
                swapped = True
        if not swapped:
            break
    return vals
