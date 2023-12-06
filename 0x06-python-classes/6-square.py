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

        self.size = size
        self.position = position

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
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and value[0] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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
