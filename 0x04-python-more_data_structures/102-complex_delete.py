#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for i in range(0, len(a_dictionary)):
        for key, val in a_dictionary.items():
            if value == val:
                del a_dictionary[key]
                break
    return a_dictionary
