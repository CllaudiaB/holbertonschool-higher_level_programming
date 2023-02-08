#!/usr/bin/python3
"""
Square #1
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Write a class Square that inherits from Rectangle
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size
