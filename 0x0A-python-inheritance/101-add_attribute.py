#!/usr/bin/python3
"""add_atribute """


def add_attribute(clase, xd, value):
    """adds attribute to object"""
    if hasattr(clase, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(clase, xd, value)
