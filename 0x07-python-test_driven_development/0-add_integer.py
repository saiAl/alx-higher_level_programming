#!/usr/bin/python3

"""
    0. Integers addition 
"""

def add_integer(a, b=98):
    """
        a function that adds 2 integers.

        Params:
            a (int): first number
            b (int): second number with defualt value equals 98

        Returns:
            the sum of the two params
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
