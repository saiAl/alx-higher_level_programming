#!/usr/bin/python3

""" Module 3-to_json_string.py """
import json


def to_json_string(my_obj):
    """
        to_json_string - a function that returns
            the JSON representation of an object

        Parameters:
            my_obj: python object

        Returns:
            JSON representation of the object
    """

    return json.dumps(my_obj)
