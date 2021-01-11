#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
"""Rectangle class"""

    def __init__(self, width=0, height=0):
        """xd"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """xd"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """xd"""
        if type(value) != int or type(value) != float:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """xd"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """xd"""
        if type(value) != int or type(value) != float:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
