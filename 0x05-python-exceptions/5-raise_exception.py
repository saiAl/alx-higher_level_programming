#!/usr/bin/python

def raise_exception():
    raise TypeError("Invalid type")

    try:
        raise_exceptionn()
    except TypeError as e:
        print("Exception raised")
