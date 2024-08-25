def let(name, val, lst):
    for i in range(len(lst)):
        if lst[i] is None:
            lst[i] = (name, val)
            return i
        elif lst[i][0] == name:
            return i
    return -1