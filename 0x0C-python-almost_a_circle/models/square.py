#!/usr/bin/python3

"""
    This module defines the Square class, which inherits
        from Rectangle and represents a square shape with
        attributes for size, coordinates, and id.
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
                self (object) : refers to the class its self
                size : size of the square
                x : x coordinates
                    (default is 0)
                y : y coordinates
                    (default is 0)
                id : integer unique value for every instance
                    (default is None)

        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """ Getter for the size attribute. """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Setter for the size attribute, to update the square's
                size by validating the provided value.

            Args:
                value : new size value
            Raises:
                TypeError if the provided value is not an integer.
                ValueError if the provided value is
                    less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value

    def update(self, *args, **kwargs):
        """
            Updates the square's attributes.

            Args:
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
        """ Returns a string representation of the square. """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size
                )

    def to_dictionary(self):
        """
            Creates a dictionary representation of the square.

            Returns:
                attrs: a dictionary includes the square's id,
                    size, x-coordinate,y-coordinate.

        """
        attrs = dict()
        for key, value in self.__dict__.items():
            attrs.update({key[11:], value})

        return attrs
