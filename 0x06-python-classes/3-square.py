#!/usr/bin/python3

"""
    3-square - module containign the Square class based on
        2-square module/class.
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

    def area(self):
        """
            area - return the current square area
        """
        return (self.__size ** 2)
