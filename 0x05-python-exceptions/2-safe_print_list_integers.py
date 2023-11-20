#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        num = 0
        leng = length(my_list)
        if (x > leng):
            raise IndexError("list index out of range")
        for idx, value in enumerate(my_list):
            if (idx < x):
                if (isinstance(value, int)):
                    print("{:d}".format(value), end='')
                    num += 1
        print()
        return num
    except TypeError:
        pass


def length(listt=[]):
    idx = 0
    for i in listt:
        idx += 1
    return idx
