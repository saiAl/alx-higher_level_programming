#!/usr/bin/python3

"""
    test module for rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ test for rectangle class """

    def test_init_with_id(self):
        """Test initializing a Rectangle object with an id"""
        expected_id = 123
        rectangle = Rectangle(width=10, height=20, id=expected_id)
        self.assertEqual(rectangle.id, expected_id)

    def test_init_without_id(self):
        """Test initializing a Rectangle object without an id"""
        expected_id = 1
        rectangle = Rectangle(width=10, height=20)
        self.assertEqual(rectangle.id, expected_id)

    def test_width_property(self):
        """Test the width property getter and setter"""
        rectangle = Rectangle(width=10, height=20)

        self.assertEqual(rectangle.width, 10)

        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)

        with self.assertRaises(TypeError):
            rectangle.width = "not an integer"

        with self.assertRaises(ValueError):
            rectangle.width = -5

    def test_height_property(self):
        """Test the height property getter and setter"""
        rectangle = Rectangle(width=10, height=20)

        self.assertEqual(rectangle.height, 20)

        rectangle.height = 30
        self.assertEqual(rectangle.height, 30)

        with self.assertRaises(TypeError):
            rectangle.height = "not an integer"

        with self.assertRaises(ValueError):
            rectangle.height = -10

    def test_x_property(self):
        """Test the x property getter and setter"""
        rectangle = Rectangle(width=10, height=20)

        self.assertEqual(rectangle.x, 0)

        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

        with self.assertRaises(TypeError):
            rectangle.x = "not an integer"

        with self.assertRaises(ValueError):
            rectangle.x = -10

    def test_y_property(self):
        """Test the y property getter and setter"""
        rectangle = Rectangle(width=10, height=20)

        self.assertEqual(rectangle.y, 0)

        rectangle.y = 15
        self.assertEqual(rectangle.y, 15)

        with self.assertRaises(TypeError):
            rectangle.y = "not an integer"

        with self.assertRaises(ValueError):
            rectangle.y = -20
    
    def test_area(self):
        """Test area calculation"""
        self.assertEqual(self.rectangle.area(), 200)

    def test_display(self):
        """Test display of the rectangle"""
        with capture_output() as output:
            self.rectangle.display()
        expected_output = "\n\n" + "#" * 10 + "\n" + "#" * 10
        self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        """Test string representation of the rectangle"""
        expected_str = "[Rectangle] ({}) {}/{} - {}/{}".format(self.rectangle.id, self.rectangle.x, self.rectangle.y, self.rectangle.width, self.rectangle.height)
        self.assertEqual(str(self.rectangle), expected_str)

    def test_update_args(self):
        """Test update method with positional arguments"""
        self.rectangle.update(2, 30, 4, 5)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 30)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 5)

    def test_update_kwargs(self):
        """Test update method with keyword arguments"""
        self.rectangle.update(height=35, y=15)
        self.assertEqual(self.rectangle.height, 35)
        self.assertEqual(self.rectangle.y, 15)

if __name__ == '__main__':
    unittest.main()
