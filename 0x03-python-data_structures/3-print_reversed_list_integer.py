#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        tope = len(my_list)
        my_list.reverse()
        for i in range(0, tope):
            print("{:d}".format(my_list[i]))
    else:
        return
