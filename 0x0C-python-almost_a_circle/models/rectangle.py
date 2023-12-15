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
            Constructor
            Args:
                width : width of the rectangle
                height : height of the rectangle
                x : x coordinate
                    (default is 0)
                y : y coordinate
                    (default is 0)
                id : instances IDs
                    (default is None)
            """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter for width
            Args:
                value: the new value to assign
            Rasies:
                TypeError: width must be an integer
                ValueError: width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter for width
            Args:
                value: the new value to assign
            Rasies:
                TypeError: width must be an integer
                ValueError: width must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter for x

            Args:
                value: the new value to assign
            Rasies:
                TypeError: x must be an integer
                ValueError: x must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter for x

            Args:
                value: the new value to assign
            Rasies:
                TypeError: x must be an integer
                ValueError: x must be > 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            Calculate the rectangle area

            Returns:
                (width * height)
        """
        return self.width * self.height

    def display(self):
        """ print hashtags to stdout """
        for j in range(self.__y):
            print()

        for i in range(self.height):
            if self.__x > 0:
                for j in range(self.__x):
                    print(' ', end='')
            print("#" * self.width)

    def __str__(self):
        """
            special method that returns special string

            Returns:
                a string contain informations about the rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            )

    def update(self, *args, **kwargs):
        """
            update the attributes

            Args:
                args : Variadic arguments
                kwargs : Keyword arguments

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
        """
            Creates a dictionary representation of the rectange.

            Returns:
                attrs: a dictionary includes the square's id,
                    size, x-coordinate,y-coordinate.

        """
        attrs = dict()

        for key, value in self.__dict__.items():
            if len(key) <= 2:
                attrs.update({key: value})
            else:
                attrs.update({key[12:]: value})
        return attrs
