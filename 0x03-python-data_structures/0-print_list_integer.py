#!/usr/bin/python3
def print_list_integer(my_list=[]):
    tope = len(my_list)
    for i in range(0, tope):
        print("{:d}".format(my_list[i]))
