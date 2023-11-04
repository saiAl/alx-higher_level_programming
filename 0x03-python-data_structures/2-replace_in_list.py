#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if my_list == None:
        return None
    if idx == None:
        return my_list

    my_list[idx] = element
    return my_list
