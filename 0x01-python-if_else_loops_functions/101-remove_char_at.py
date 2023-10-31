#!/usr/bin/python3

def remove_char_at(str, n):
    new = ''
    for idx, value in enumerate(str):
        if idx == n:
            continue
        else:
            new += value
    return new
