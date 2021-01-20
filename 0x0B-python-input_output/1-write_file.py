#!/usr/bin/python3
""" class Student """


def write_file(filename="", text=""):
    """ class Student """
    cont = 0
    with open(filename, "w") as file:
        file.write(text)
    return (len(text))
