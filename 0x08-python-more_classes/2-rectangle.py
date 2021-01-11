#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class rectangle """
    def __init__(self, width=0, height=0):
        """ iniciar """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ returns width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set width """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set height """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area """
        return (self.width * self.height)

    def perimeter(self):
        """ returns the perimeter """
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * self.width) + (2 * self.height)
