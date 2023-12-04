#!/usr/bin/python3

"""
    Module 2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """
        a function that returns True if the object is exactly
            an instance of the specified class ; otherwise False.

        Parameters:
            obj (Object):
            a_class (class):
    """

    if type(obj) == a_class:
        return True
    else:
        return False
