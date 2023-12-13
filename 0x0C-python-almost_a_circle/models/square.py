#!/usr/bin/python3

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
        """
        Args:
            self (object) : Argument
            size : Argument
            x : Argument
                (default is 0)
            y : Argument
                (default is 0)
            id : Argument
                (default is None)

        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """
        Args:
            self (object) : Argument

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            self (object) : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value

    def update(self, *args, **kwargs):
        """
        Args:
            self (object) : Argument
            args : Variadic arguments
            kwargs : Keyword arguments

        """
        if args:
            for idx, arg in enumerate(args):
                setattr(self, ["id", "size", "x", "y"][idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Args:
            self (object) : Argument

        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size
                )

    def to_dictionary(self):
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

        return attrs
