#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """inherits from function"""
    if type(obj) is a_class:
        return (False)
    else:
        return issubclass(type(obj), a_class)
