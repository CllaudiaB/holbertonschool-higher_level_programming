#!/usr/bin/python3
"""
Defines a square
"""


class Square:
    """
    That defines a square by: based on 2-square.py
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        That returns the current square area
        """
        square_area = self.__size
        return square_area * square_area
