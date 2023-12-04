#!/usr/bin/python3

"""
    Module 0-lookup.py
"""


def lookup(obj):
    """
        a function that returns the list of available
            attributes and methods of an object.

        Parameters:
            obj (Object): an object.
        Returns:
            return a list of avaliable attributes and meethod.
    """

    return dir(obj)
