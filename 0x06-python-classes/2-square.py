#!/usr/bin/python3

"""
    2-square - module containign the Square class based on
        1-square module/class.
"""


class Square:
    """
        Square - class of Square'
    """
    def __init__(self, size=0):
        """
            size: private instance attribute.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
