#!/usr/bin/python3

""" Module 4-from_json_string.py """
import json


def from_json_string(my_str):
    """
        from_json_string - a function that returns an object
            represented by a JSON string

        Parameters:
            my_str (str): JSON string

        Returns:
            python object
    """

    return json.loads(my_str)
