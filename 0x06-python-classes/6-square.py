#!/usr/bin/python3

"""
    5-square - module containign the Square class based on
        4-square module/class.
"""


class Square:
    """
        Square - class of Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
            size: private instance attribute.
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__value

    @position.setter
    def position(self, value):
        self.__value = value

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
        elif len(self.__position) > 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            ver = self.__position[1]
            hor = self.__position[0]

            for i in range(ver):
                print()

            for i in range(self.__size):
                for h in range(hor):
                    print(' ', end='')

                for j in range(self.__size):
                    print("#", end='')
                print()
