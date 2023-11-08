#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_list = list()
    for key, value in a_dictionary.items():
        new_list.append((key, value * 2))
    
    new_dict = dict(new_list)
    return new_dict

