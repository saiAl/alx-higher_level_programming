#!/usr/bin/python3

"""
    5-square - module containign the Square class based on
        4-square module/class.
"""


class Square:
    """
        Square - class of Square
    """
    def __init__(self, size=0):
        """
            size: private instance attribute.
        """

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
            area - return the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
            my_print - print # symbol
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
