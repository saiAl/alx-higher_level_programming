#!/usr/bin/python3

""" Module 8-class_to_json.py """


def class_to_json(obj):
    """
        class_to_json - a function that returns the dictionary
            description with simple data structure

        Parameters:
            obj: an instance of a Class
        Returns:
            the dictionary description
    """
    return obj.__dict__
