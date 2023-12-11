#!/usr/bin/python3
"""
    This module defines the Rectangle class, which inherits from the Base
        class and represents a rectangle with attributes for width, height, x
        coordinate, and y coordinate.

"""
from models.base import Base


class Rectangle(Base):
    """
        Class representing a rectangle with attributes for width, height,
        x coordinate, and y coordinate. It inherits from the Base class
        and automatically manages its id attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            constructor for Rectangle class

            args:
                width (int): width of the rectangle
                height (int): height of the rectangle
                x (int): the x coordinates
                y (int): the y coordinates
                id : unique identifier, inhertied form
                    Base using super() method
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter for the width attribute

            args:
                value (int): the new value of width

            raises:
            TypeError: if value not of type int
            ValueError: if value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter for the height attribute

            args:
                value (int): the new value of height

            raises:
            TypeError: if value not of type int
            ValueError: if value is less or equal to 0.
         """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ getter for the x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter for the x attribute

            args:
                value (int): the new value of x

            raises:
            TypeError: if value not of type int
            ValueError: if value is less then 0.
         """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter for the y attribute

            args:
                value (int): the new value of y

            raises:
            TypeError: if value not of type int
            ValueError: if value is less then 0.
         """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            public method that returns the area value

            returns:
                the area value of Rectangle instance.
        """

        return (self.__width * self.__height)

    def display(self):
        """
            public method that prints in stdout the rectangle instance
                with character #
        """
        for j in range(self.__y):
            print()

        for i in range(self.__height):
            if self.__x > 0:
                for j in range(self.__x):
                    print(' ', end='')
            print("#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x,
            self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            public method that assigns an argument to each attribute

            args:
                args: a positional argument
                kwargs: a keyword argument
        """
        if args:
            for idx, arg in enumerate(args):
                setattr(self, ["id", "width", "height", "x", "y"][idx], arg)
        elif kwargs:
            keys = list()
            values = list()
            for key, value in kwargs.items():
                keys.append(key)
                values.append(value)

            for idx in range(len(keys)):
                setattr(self,  keys[idx], values[idx])

    def to_dictionary(self):
        """ Document this method """
        return self.__dict__
