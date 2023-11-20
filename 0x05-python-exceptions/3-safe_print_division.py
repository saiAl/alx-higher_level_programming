#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = float()
        if (b == 0):
            res = None
            return None
        else:
            res = (a / b)
            return res
    finally:
        if res is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(res))
