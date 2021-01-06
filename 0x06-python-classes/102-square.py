#!/usr/bin/python3
'''Square class'''


class Square:
    '''size instantiation'''
    def __init__(self, size=0):
        self.__size = size

    '''Size getter'''
    @property
    def size(self):
        return self.__size

    '''Size setter'''
    @size.setter
    def size(self, value):
        if not type(value) is int or not type(value) is float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    '''Returns the area of the square'''
    def area(self):
        return self.__size ** 2

    def __lt__(self, other):
        '''p1 < p2 calls p1.__lt__(p2)'''
        return self.__size ** 2 < other.__size ** 2

    def __eq__(self, other):
        '''p1 == p2 calls p1.__eq__(p2)'''
        return self.__size ** 2 == other.__size ** 2

    def __ne__(self, other):
        '''p1 != p2 calls p1.__eq__(p2)'''
        return self.__size ** 2 != other.__size ** 2

    def __le__(self, other):
        '''p1 <= p2 calls p1.__le__(p2)'''
        return self.__size ** 2 <= other.__size ** 2

    def __gt__(self, other):
        '''p1 > p2 calls p1.__gt__(p2)'''
        return self.__size ** 2 > other.__size ** 2

    def __ge__(self, other):
        '''p1 >= p2 calls p1.__ge__(p2)'''
        return self.__size ** 2 >= other.__size ** 2
