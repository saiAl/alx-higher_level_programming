#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = list()
    for idx, value in enumerate(my_list):
        if value == search:
            new.append(replace)
        else:
            new.append(value)
        
    return new
