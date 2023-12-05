#!/usr/bin/python3

"""Module 1-write_file.py"""


def write_file(filename="", text=""):
    """
        write_file - a function that writes a string to a text file
            and returns the number of characters written

        Parameters:
            filename: path to the file.
            text: bytes to write in the file

        Returns:
            number of bytes written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        data = f.write(text)

    return data
