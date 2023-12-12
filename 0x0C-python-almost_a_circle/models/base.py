#!/usr/bin/python3

"""
    This module containing the Base class of all other classes in this
        package, The goal of this class is to manage id attribute in all
        the classes and to avoid duplicating the same code
"""


class Base:
    """
        The base class

        Attributes:
            __nb_object (int): his private class attribute
                keeps track of the total number of created Base objects.
        Methods:
            __init__ method:
                if an id argument is provided, it's assigned
                    to the public instance attribute self.id.
                Otherwise, __nb_objects is incremented and the
                    new value is assigned to self.id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor for Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Document this static method """
        import json

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
