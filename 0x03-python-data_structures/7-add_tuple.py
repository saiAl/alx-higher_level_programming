#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = list()
    b = list()
    new = list()

    a = check_tuple(list(tuple_a))
    b = check_tuple(list(tuple_b))

    for i in range(2):
        res = a[i] + b[i]
        new.append(res)
    return tuple(new)


def check_tuple(list_c=[]):
    new = list()
    if len(list_c) < 2:
        if len(list_c) == 0:
            for i in range(1):
                list_c.append(0)
        for i in range(len(list_c)):
            list_c.append(0)
    if len(list_c) > 2:
        for i in range(2):
            new.append(list_c[i])
        return new

    return list(list_c)
