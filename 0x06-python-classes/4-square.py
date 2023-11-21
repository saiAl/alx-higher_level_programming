#!/usr/bin/python3

"""
    4-square - module containign the Square class based on
        3-square module/class.
"""


class Square:
    """
        Square - class of Square
    """
    def __init__(self, size=0):
        """
            size: private instance attribute.
        """

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def area(self):
        """
            area - return the current square area
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

        return (self.__size * self.__size)
