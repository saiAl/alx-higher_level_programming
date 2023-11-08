#!/usr/bin/python3

def best_score(a_dictionary):
    big = 0
    if a_dictionary is None:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > big:
                big = value
        for k, v in a_dictionary.items():
            if big == v:
                return k
