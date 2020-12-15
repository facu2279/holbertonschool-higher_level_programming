#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        tope = len(my_list)
        for i in range(tope - 1, -1, -1):
            print("{:d}".format(my_list[i]))
    else:
        return
