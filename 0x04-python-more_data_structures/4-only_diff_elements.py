#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_3 = list()

    for i in set_1:
        set_3.append(i)
    for i in set_2:
        set_3.append(i)
    return set(set_3)
