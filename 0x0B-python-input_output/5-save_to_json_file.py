#!/usr/bin/python3
""" class Student """
import json


def save_to_json_file(my_obj, filename):
    """ class Student """
    with open(filename, "w") as file:
            file.write(json.dumps(my_obj))
