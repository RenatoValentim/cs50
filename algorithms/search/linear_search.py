def linear_search(val, vals):
    for i in range(len(vals)):
        if val == vals[i]:
            return True, i
    return False, -1
