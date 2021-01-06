#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square class"""
    __size = None

    def __init__(self, size=0):
        """__init__"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
