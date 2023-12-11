#!/usr/bin/python3

""" Tests module for tasks task 0 """
from models.base import Base
import unittest
import os


class testBase(unittest.TestCase):
    """ testBase containing test cases for Base """

    def test_existing_file(self):
        """Test if an existing file is detected"""
        file_path = os.path.exists("models/base.py")
        self.assertTrue(os.path.exists(file_path))

    def test_init_with_id(self):
        """ checks if __init__ correctly assigns the provided ID """

        obj = Base(id=3)
        self.assertEqual(obj.id, 3)

    def test_init_without_id(self):
        """ checks __init__ correctly excute without assigning ID """

        obj = Base()
        self.assertEqual(obj.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)


if __name__ == '__main__':
    unittest.main()
