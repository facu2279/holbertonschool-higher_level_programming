#!/usr/bin/python3
"""class student"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """iniciar"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
