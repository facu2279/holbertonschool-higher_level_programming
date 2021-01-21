#!/usr/bin/python3
""" append after """


def append_after(filename="", search_string="", new_string=""):
    """ append after """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for i in lines:
            if search_string in i:
                file.write(i + new_string)
            else:
                file.write(i)
