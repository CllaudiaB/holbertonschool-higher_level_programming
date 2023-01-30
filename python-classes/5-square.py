#!/usr/bin/python3
"""
Defines a square
"""


class Square:
    """
    That defines a square by: based on 4-square.py
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current square area
        """
        square_area = self.__size
        return square_area * square_area

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
