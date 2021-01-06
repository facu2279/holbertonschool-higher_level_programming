#!/usr/bin/python3
'''Square class'''


class Square:
    '''size and position instantiation'''
    def __init__(self, size=0, position=(0, 0)):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not type(position) is tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not type(position[0]) is int) or (not type(position[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    '''Size getter'''
    @property
    def size(self):
        return self.__size

    '''Size setter'''
    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    '''Position getter'''
    @property
    def position(self):
        return self.__position

    '''Position Setter'''
    @position.setter
    def position(self, value):
        if not type(value) is tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not type(value[0]) is int) or (not type(value[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    '''Returns the area of the square'''
    def area(self):
        return self.__size ** 2

    '''Prints the square'''
    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for l in range(0, self.__position[1]):
                print()

        for i in range(0, self.__size):
            if self.__position[0] > 0:
                for k in range(0, self.__position[0]):
                    print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    def __str__(self):
        sqr = ""
        if self.__size == 0:
            return sqr
        if self.__position[1] > 0:
            for l in range(0, self.__position[1]):
                sqr += "\n"
        for i in range(0, self.__size):
            if self.__position[0] > 0:
                for k in range(0, self.__position[0]):
                    sqr += " "
            for j in range(0, self.__size):
                sqr += "#"
            if i < self.__size - 1:
                sqr += "\n"
        return sqr
