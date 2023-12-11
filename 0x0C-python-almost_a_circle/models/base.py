#!/usr/python3

"""
    This module containing the Base class of all other classes in this
    package, The goal of this class is to manage id attribute in all
    the classes and to avoid duplicating the same code
"""


class Base():
    """
        The base class

        Attributes:
            __nb_object (int): private class attribute
        Methods:
            __init__(): class constructor to initilize Base instances with id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
