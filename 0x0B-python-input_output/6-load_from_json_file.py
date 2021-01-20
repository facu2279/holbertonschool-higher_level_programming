#!/usr/bin/python3
""" class Student """
import json


def load_from_json_file(filename):
    """ class Student """
    with open(filename) as file:
        return (json.load(file))
