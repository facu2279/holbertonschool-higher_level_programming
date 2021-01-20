#!/usr/bin/python3
""" class Student """


def write_file(filename="", text=""):
    """ class Student """
    cont = 0
    with open(filename, "w") as file:
        for line in text:
            cont = cont + len(line)
        return (cont)
