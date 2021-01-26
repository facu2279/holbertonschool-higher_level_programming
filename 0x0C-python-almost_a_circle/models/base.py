#!/usr/bin/python3
""" define a class Base """
import json


class Base:
    """ class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """define new object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = self.__nb_objects + 1
            self.id = self.__nb_objects
    

    def intvalidator(self, name, value):
        """ this function check if value is a good type """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
        elif value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))
    
    def to_json_string(list_dictionaries):
        """ return string """
        if list_dictionaries == None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        filename = cls.__name__ + ".json"
        lista = []
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write(lista)
            else:
                for obj in list_objs:
                    lista.append(cls.to_dictionary(obj))
                lista = Base.to_json_string(lista)
                file.write(lista)
    
    def from_json_string(json_string):
        """ class Student """
        string = []
        if json_string is not None and json_string == "":
            string = json.loads(json_string)
        return (string)