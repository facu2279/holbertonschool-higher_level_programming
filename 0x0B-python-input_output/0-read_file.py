#!/usr/bin/python3
""" class Student """


def read_file(filename=""):
    """ class Student """
    with open(filename) as file:
        for line in file:
            print(line, end="")
