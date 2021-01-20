#!/usr/bin/python3
""" class Student """


def append_write(filename="", text=""):
    """ class Student """
    with open(filename, "a") as file:
            file.write(text)
    return (len(text))
