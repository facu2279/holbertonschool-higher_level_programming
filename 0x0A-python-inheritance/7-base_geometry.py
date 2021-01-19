#!/usr/bin/python3
"""base_geometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that check if the value is integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
