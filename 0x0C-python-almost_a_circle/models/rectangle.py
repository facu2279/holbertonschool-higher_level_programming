#!/usr/bin/python3
""" defines a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ def """
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
        return self.width
    @property
    def height(self):
        return self.height
    @property
    def x(self):
        return self.x
    @property
    def y(self):
        return self.y

    @width.setter
    def width(self, value):
        self.intvalidator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.intvalidator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.intvalidator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.intvalidator("y", value)
        self.__y = value
    
    def area(self):
        return (self.__width * self.__height)
    
    def display(self):
        for i in range(self.__y):
            print("")
        for i2 in range(self.__height):
            for i3 in range(self.__x):
                print(" ", end = "")
            for i4 in range(self.__width - 1):
                print("#", end = "")
            print("#")
    
    def __str__(self):
        """ def """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
        self.__y, self.__width, self.__height)
