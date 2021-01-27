#!/usr/bin/python3
""" define a class Base """
import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return string """
        if list_dictionaries is None:
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

    @staticmethod
    def from_json_string(json_string):
        """ class Student """
        string = []
        if json_string is not None and json_string == "":
            string = json.loads(json_string)
        return (string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if (cls.__name__ == "Square"):
            a = cls(1)
        elif (cls.__name__ == "Rectangle"):
            a = cls(1, 1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        lists = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                for obj in cls.from_json_string(f.read()):
                    lists.append(cls.create(**obj))
                return lists
        except Exception:
            return lists

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file csv function """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            csv_write = csv.writer(f, delimiter=',')
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_write.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_write.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ class load from file """
        lists = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                csv_reader = csv.reader(f, delimiter=',')
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]), "height": int(
                            args[2]), "x": int(args[3]), "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(
                            args[1]), "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    lists.append(obj)
                return (lists)
        except Exception:
            return (lists)
