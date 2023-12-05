#!/usr/bin/python3

""" Module 2-append_write.py """


def append_write(filename="", text=""):
        """
            append_write - a function that appends a string at the end of a text file
                and returns the number of characters added

            Parameters:
                filename: path to the file
                text: text to append to the file

            Returns:
                number of bytes added to the file
        """

        with open(filename, 'a', encoding="utf-8") as f:
            data = f.write(text)

        return data
