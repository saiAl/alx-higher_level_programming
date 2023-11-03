#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = list()
    b = list()
    new = list()

    a = list(tuple_a)
    b = list(tuple_b)

    if len(a) < 2:
        if len(b) == 0:
            for i in range(1):
                b.append(0)
        for i in range(len(a)):
            a.append(0)

    if len(b) < 2:
        if len(b) == 0:
            for i in range(1):
                b.append(0)
        for i in range(len(b)):
            b.append(0)

    for i in range(len(a)):
        res = a[i] + b[i]
        new.append(res)

    return tuple(new)
