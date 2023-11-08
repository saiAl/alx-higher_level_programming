#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_3 = list()

    for i in set_1:
        if i in set_2:
            continue
        else:
            set_3.append(i)

    for i in set_2:
        if i in set_1:
            continue
        else:
            set_3.append(i)

    return set(set_3)
