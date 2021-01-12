#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class Rectangle """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ iniciar """
        self.height = height
        self.width = width
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __str__(self):
        """ return rectangle """
        rep = ""
        if not self.area():
            return (rep)
        for row in range(self.height):
            rep = rep + str(self.print_symbol) * self.width
            if row != self.height - 1:
                rep = rep + "\n"
        return (rep)

    def __repr__(self):
        """ return string """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ delete """
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    @classmethod
    def square(cls, size=0):
        """ returns rectangle """
        if not type(size) is int:
            raise TypeError("size must be an int")
        if size < 0:
            raise ValueError("size must be >= 0")
        return (Rectangle(size, size))

    def bigger_or_equal(rect_1, rect_2):
        """ method to compare rectangles """
        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an isntance of Rectangle")
        area_1 = self.area(rect_1)
        area_2 = self.area(rect_2)
        if area_1 >= area_2:
            return (rect_1)
        else:
            return (rect_2)

    @property
    def width(self):
        """ returns width """
        return (self.__width)

    @width.setter
    def width(self, value):
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
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area """
        return (self.width * self.height)

    def perimeter(self):
        """ returns perimeter"""
        if self.area() == 0:
            return (0)
        return (2 * self.width) + (2 * self.height)
