#!/usr/bin/python3
"""
How many instances
"""


class Rectangle:
    """
    That defines a rectangle by: based on 4-rectangle.py and return area \
    and perimeter and print the rectangle with character #
    Print the message Bye rectangle... (... being 3 dots not ellipsis) when \
    an instance of Rectangle is deleted
    """

    counter = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.counter += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += '#'
                rectangle += '\n'
        return rectangle[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.counter -= 1
        print("Bye rectangle...")
