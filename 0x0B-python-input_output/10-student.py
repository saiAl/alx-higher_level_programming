#!/usr/bin/python3

""" Module  10-student.py based on 9-student.py """


class Student:
    """
        a class that defines a student by
            first_name
            last_name
            age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation
                of a Student instance
        """
        new = {}

        if attrs is None:
            return self.__dict__
        else:
            for key, value in self.__dict__.items():
                if key in attrs:
                    new[key] = value
            return new
