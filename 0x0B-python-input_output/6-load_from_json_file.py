#!/usr/bin/python3

""" Module 6-load_from_json_file.py """
import json


def load_from_json_file(filename):
    """
        load_from_json_file - a function that creates an Object
            from a JSON file

        Parameters:
            filename: path to the file

        Returns:
            python object
    """

    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data
