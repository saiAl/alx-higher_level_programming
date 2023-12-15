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
        Args:
            self (object) : Argument
            width : Argument
            height : Argument
            x : Argument
                (default is 0)
            y : Argument
                (default is 0)
            id : Argument
                (default is None)

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Args:
            self (object) : Argument

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Args:
            self (object) : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Args:
            self (object) : Argument

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
            self (object) : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Args:
            self (object) : Argument

        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Args:
            self (object) : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Args:
            self (object) : Argument

        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Args:
            self (object) : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Args:
            self (object) : Argument

        """
        return self.width * self.height

    def display(self):
        """
        Args:
            self (object) : Argument

        """
        for j in range(self.__y):
            print()

        for i in range(self.height):
            if self.__x > 0:
                for j in range(self.__x):
                    print(' ', end='')
            print("#" * self.width)

    def __str__(self):
        """
        Args:
            self (object) : Argument

        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
            )

    def update(self, *args, **kwargs):
        """
        Args:
            self (object) : Argument
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

'''    def to_dictionary(self):
        """
        Args:
            self (object) : Argument

        """
        attrs = dict()
        for key, value in self.__dict__.items():
            match key:
                case "_Rectangle__width":
                    attrs.update({"width": value})
                case "_Rectangle__height":
                    attrs.update({"height": value})
                case "_Rectangle__x":
                    attrs.update({"x": value})
                case "_Rectangle__y":
                    attrs.update({"y": value})
                case "id":
                    attrs.update({"id": value})

        return attrs'''
