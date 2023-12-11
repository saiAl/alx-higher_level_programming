#!usr/bin/python3

""" Document this module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Document this class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Document the method"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    @property
    def width(self):
        return self.__size
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__size = value

    @property
    def height(self):
        return self.__size

    @height.setter
    def height(self, value):
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
        """ Document this method """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)


