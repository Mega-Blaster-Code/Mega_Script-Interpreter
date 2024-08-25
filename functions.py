def find_var(name, lst):
    for i in range(len(lst)):
        if lst[i] is not None and lst[i][0] == name:
            return i
    for i in range(len(lst)):
        if lst[i] is None:
            return i
    return -1