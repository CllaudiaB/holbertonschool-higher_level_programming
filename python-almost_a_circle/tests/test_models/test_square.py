#!/usr/bin/python3
"""
Test square
"""
import unittest
from models.square import Square
from models.base import Base


class Test_Square(unittest.TestCase):
    def test_init(self):
        """
        Test instance attributes
        """
        s = Square(8, 6, 4, 18)
        self.assertEqual(s.id, 18)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 4)
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        s = Square(1)
        self.assertEqual(s.size, 1)
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_type_error(self):
        """
        Test TypeError
        """
        with self.assertRaises(TypeError) as cm:
            s1 = Square("1")
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(TypeError) as cm:
            s1 = Square(1, "2")
        self.assertEqual(str(cm.exception), "x must be an integer")

        with self.assertRaises(TypeError) as cm:
            s1 = Square(1, 2, "3")
        self.assertEqual(str(cm.exception), "y must be an integer")

    def test_type_value(self):
        """
        Test ValueError
        """
        with self.assertRaises(ValueError) as cm:
            s1 = Square(-1)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            s1 = Square(1, -2)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            s1 = Square(1, 2, -3)
        self.assertEqual(str(cm.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as cm:
            s1 = Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")
