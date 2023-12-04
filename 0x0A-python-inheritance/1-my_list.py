#!/usr/bin/python3

"""
    Module 1-my_list.py
"""


class MyList(list):
    """
        MyList is a class that inherits from list Object.
    """

    def print_sorted(self):
        """
            Public method that prints the list sorted

        """
        new = self.copy()
        new.sort()
        print(new)
