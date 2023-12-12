#!usr/bin/python3

"""
    This module defines the Square class, which inherits
        from the Rectangle class and represents a square with
        attributes for size, x coordinate, y coordinate, and id.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        The Square class represents a square with attributes for size
            (which determines both width and height), x coordinate,
            y coordinate, and id. It inherits all functionalities
            from the Rectangle class and adds specific methods
            and properties related to its square shape.

        methods:
            __init__: constructor initializes the Square object
                with the provided size, x and y coordinates,
                and optional id. It inherits the Rectangle
                constructor to set the width and height equal
                to the provided size.

            property width, height: property getter
                returns the current value of the Square's size
                attribute, which represents both its width and height.

            width.setter, height.setter: This setter allows updating
                the Square's size attribute by validating the provided
                value It updates both the width and height
                attributes with the new size value.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Square's class constructor """
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def width(self):
        """
            getter returns the current value of the
                Square's size attribute
        """
        return self.__size

    @width.setter
    def width(self, value):
        """
            setter to update and validate the Square's size attribute

            args:
                value (int): the new size value
            raises:
                TypeError: if value not of type int
                ValueError: if value less then 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value

    @property
    def height(self):
        """
            getter returns the current value of the
                Square's size attribute
        """
        return self.__size

    @height.setter
    def height(self, value):
        """
            setter to update and validate the Square's size attribute

            args:
                value (int): the new size value
            raises:
                TypeError: if value not of type int
                ValueError: if value less then 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__size= value

    def update(self, *args, **kwargs):
        """
            public method that assigns an argument to each attribute

            args:
                args: a positional argument
                kwargs: a keyword argument
        """
        if args:
            for idx, arg in enumerate(args):
                setattr(self, ["id", "size", "x", "y"][idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
            method to returns a string representation of the
                Square object, including its id, x and y
                coordinates, and size.
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size
                )
