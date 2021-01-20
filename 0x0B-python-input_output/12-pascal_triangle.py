#!/usr/bin/python3
""" pascal """


def pascal_triangle(n):
    """ pascal triangle for the win """
    my_list = []
    if n <= 0:
        return my_list

    my_list
    a = 1
    for i in range(1, n + 1):
        if i == 1:
            my_list.append(str(a))
        else:
            a = (a + (a * 10))
            my_list.append(str(a))
    return my_list
