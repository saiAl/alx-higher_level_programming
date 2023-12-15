#!/usr/bin/python3

"""
    This module containing the Base class of all other classes in this
        package, The goal of this class is to manage id attribute in all
        the classes and to avoid duplicating the same code
"""
import json


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

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file

            Args:
                list_objs: is a list of instances who inherits of Base
        """
        file_name = "{:s}.json".format(cls.__name__)
        with open(file_name, 'w', encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.close()
            else:
                dict_objs = dict()

                for obj in list_objs:
                    for key, value in obj.__dict__.items():
                        if len(key) <= 2:
                            dict_objs.update({key: value})
                        elif f'_{cls.__name__}__{key[3 + len(cls.__name__):]}' in key:
                            dict_objs.update(
                                    {key[3 + len(cls.__name__):]: value}
                                    )
                        else:
                            dict_objs.update({key[12:]: value})

                data = cls.to_json_string([dict_objs for obj in list_objs])
                print(data)
