#!/usr/bin/python3


def max_integer(my_list=[]):
    n = my_list[0]

    for i in my_list:
        if n > i:
            continue
        else:
            n = i

    return n
