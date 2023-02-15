#!/usr/bin/python3
"""
Test rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from contextlib import redirect_stdout

class Test_Rectangle(unittest.TestCase):
    def test_init(self):
        """
        Test instance attributes
        """
        r = Rectangle(8, 6, 4, 2, 18)
        self.assertEqual(r.id, 18)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 2)
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_type_error_init(self):
        """
        Test TypeError
        """
        with self.assertRaises(TypeError) as cm:
            r1 = Rectangle("8", 6, 4, 2, 18)

        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
             r1 = Rectangle(8, "6", 4, 2, 18)

        self.assertEqual(str(cm.exception), "height must be an integer")

        with self.assertRaises(TypeError) as cm:
             r1 = Rectangle(8, 6, "4", 2, 18)

        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
             r1 = Rectangle(8, 6, 4, "2", 18)

        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_value_error_init(self):
        """
        Test ValueError
        """
        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(-8, 6, 4, 2, 18)

        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(8, -6, 4, 2, 18)

        self.assertEqual(str(cm.exception), "height must be > 0")

        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(8, 6, -4, 2, 18)

        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(8, 6, 4, -2, 18)

        self.assertEqual(str(cm.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(0, 2)

        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            r1 = Rectangle(1, 0)

        self.assertEqual(str(cm.exception), "height must be > 0")

    def test_area(self):
        """
        Test area
        """
        r2 = Rectangle(3, 2)
        self.assertEqual(r2.area(), 6)

    def test_str(self):
        """
        Test str
        """
        r = Rectangle(8, 6, 4, 2, 18)
        self.assertEqual(str(r), "[Rectangle] (18) 4/2 - 8/6")

    def test_display(self):
        """
        Test display rectangle
        """
        r3 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            r3.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

        r3 = Rectangle(3, 2, 1, 1)
        expected_output = "\n ###\n ###\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            r3.display()
            result = buffer.getvalue()
        self.assertEqual(result, expected_output)

    def test_update(self):
        """
        Test update
        """
        r = Rectangle(8, 6, 4, 2, 18)
        r.update(89, 10, 10, 10, 10)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_dictionary(self):
        r = Rectangle(8, 6, 4, 2, 18)
        self.assertEqual(r.to_dictionary(), { "id": 18, "width": 8, "height": 6,
                                           "x": 4, "y": 2})