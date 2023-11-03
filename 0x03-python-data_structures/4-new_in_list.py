#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return copy
    if idx > len(my_list):
        return copy

    for i, value in enumerate(my_list):
        if i == idx:
            copy[i] = element
    return copy
