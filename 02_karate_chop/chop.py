def chop_walk(i, iArray):
    if len(iArray) == 0:
        return -1

    counter = 0
    for a in iArray:
        if a == i:
            return counter
        counter += 1
    return -1
