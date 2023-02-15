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
        self.assertEqual(r.id, 18)
        self.assertEqual(r.size, 8)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 4)
        s = Square(1, 2, 3)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
