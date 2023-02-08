#!/usr/bin/python3
"""
Square #2
"""


Rectangle = __import__('9-rectangle').Rectangle


class Squrae(Rectangle):
    """
    Class Square that inherits from Rectangle and return area
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Sqaure] {}/{}".format(self.__size, self.__size)
