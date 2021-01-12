#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ iniciar """
        self.height = height
        self.width = width
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """return width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ return height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set height"""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """return area"""
        return(self.__width * self.__height)

    def perimeter(self):
        """return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ return string """
        newone = ""
        if self.__width == 0 or self.__height == 0:
            return (newone)
        if not type(self.print_symbol) is str:
            self.print_symbol = str(self.print_symbol)
        for width in range(self.__height - 1):
            newone = newone + (self.print_symbol * self.__width) + '\n'
        newone = newone + (self.print_symbol * self.__width)
        return (newone)

    def __repr__(self):
        """define repr"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ delete """
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the big rectangle"""
        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """returns new rectangle"""
        return (Rectangle(size, size))
