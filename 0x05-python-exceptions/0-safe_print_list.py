#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for idx, value in enumerate(my_list):
            if (idx < x):
                print(value, end='')
                num += 1
        print()
        return num
    except:
        pass
