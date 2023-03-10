#!/usr/bin/python3
"""
Unittest for class Base
"""
import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    """
    Unittest to check the class Base
    """
    def test_init(self):
        """
        Tests attribute id
        """
        b = Base()
        self.assertEqual(b.id, 1)

        b1 = Base()
        self.assertEqual(b1.id, 2)

        b2 = Base(30)
        self.assertEqual(b2.id, 30)
