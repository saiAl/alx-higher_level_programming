#!/usr/bin/python3

"""
    Module 3-is_kind_of_class.py
"""


def inherits_from(obj, a_class):
    """
        a function that returns True if the object is an instance of,
            or if the object is an instance of a class that inherited from,
            the specified class ; otherwise False.

        Parameters:
            obj (Object):
            a_class (class):
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
