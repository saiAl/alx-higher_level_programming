#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = float()
        if (b == 0):
            raise Exception
            return None
        else:
            res = (a / b)
            return res
    except Exception:
        res = None
    finally:
        if res is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.1f}".format(res))
