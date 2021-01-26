#!/usr/bin/python3
""" defines a class Rectangle """
from models.base import Base
import sys
import csv

class Rectangle(Base):
    """ class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ def init """
        self.intvalidator("height", height)
        self.__height = height
        self.intvalidator("width", width)
        self.__width = width
        self.intvalidator("x", x)
        self.__x = x
        self.intvalidator("y", y)
        self.__y = y
        self.id = id
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        """ def width """
        return self.__width

    @property
    def height(self):
        """ def height """
        return self.__height

    @property
    def x(self):
        """ def x """
        return self.__x

    @property
    def y(self):
        """ def y """
        return self.__y

    @width.setter
    def width(self, value):
        """ set width """
        self.intvalidator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        self.intvalidator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """ set y """
        self.intvalidator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """ set y """
        self.intvalidator("y", value)
        self.__y = value

    def area(self):
        """ calculate area """
        return (self.__width * self.__height)

    def display(self):
        """ print in screen """
        for i in range(self.__y):
            print("")
        for i2 in range(self.__height):
            for i3 in range(self.__x):
                print(" ", end="")
            for i4 in range(self.__width - 1):
                print("#", end="")
            print("#")

    def __str__(self):
        """ parse objetct to str """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ class upadate an object """
        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.intvalidator("width", args[1])
                self.__width = args[1]
            if len(args) > 2:
                self.intvalidator("height", args[2])
                self.__height = args[2]
            if len(args) > 3:
                self.intvalidator("x", args[3])
                self.__x = args[3]
            if len(args) > 4:
                self.intvalidator("y", args[4])
                self.__y = args[4]
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "width":
                    self.intvalidator("width", val)
                    self.__width = val
                if key == "height":
                    self.intvalidator("height", val)
                    self.__height = val
                if key == "x":
                    self.intvalidator("x", val)
                    self.__x = val
                if key == "y":
                    self.intvalidator("y", val)
                    self.__y = val

    def to_dictionary(self):
        """ create a dictionary """
        my_dictionary = {"x": self.__x, "y": self.__y, "id": self.id,
                         "width": self.__width, "height": self.__height}
        return (my_dictionary)
