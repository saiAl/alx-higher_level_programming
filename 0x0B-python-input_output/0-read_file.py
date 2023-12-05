#!/usr/bin/python3

""" Module 0-read_file.py """


def read_file(filename=""):
    """
        read_file - a function that reads a text file
            and prints it to stdout

        Parameters:
            filename: path to the file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
    print(data)
