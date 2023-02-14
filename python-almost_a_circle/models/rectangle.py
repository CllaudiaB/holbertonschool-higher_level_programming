#!/usr/bin/python3
"""
First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Write the class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        That prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for k in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
         Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
        That assigns an argument to each attribute
        """
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.width = v
                if i == 2:
                    self.height = v
                if i == 3:
                    self.x = v
                if i == 4:
                    self.y = v
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
