#!/usr/bin/python3
"""Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ class Square from Rectangle from BaseGeometry"""
    def __init__(self, size):
        """Iniciar"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
