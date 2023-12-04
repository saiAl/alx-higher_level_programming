#!/usr/bin/python3

"""
    Module 7-base_geometry.py based on 6_geometry.py
"""


class BaseGeometry:
    """
        BaseGeometry - an empty class
    """

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        
        if not isinstance(self.value, int):
            raise TypeError("{:s} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(self.name))

    def area(self):
        raise Exception("area() is not implemented")
