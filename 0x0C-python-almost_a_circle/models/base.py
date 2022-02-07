#!/usr/bin/python3
"""base.py
Module containing the class Base.
"""


import json
import os


class Base:
    """The class Base is the 'base' of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to
    avoid duplicating the same code (by extension, same bugs).
    __nb_objects: private class attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """The __init__ method is called when a new instance is created.
        Args:
        id: (always an integer) public instance attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write(cls.to_json_string(None))
            else:
                my_list = []
                for i in range(len(list_objs)):
                    my_list.append(list_objs[i].to_dictionary())
                f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2, 1)
        if cls.__name__ == 'Square':
            dummy = cls(2, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename) is False:
            return []
        else:
            with open(filename, "r") as my_file:
                read = my_file.read()
                dicst = cls.from_json_string(read)
                instance_list = []
                for i in dicst:
                    instance_list.append(cls.create(**i))
                return instance_list
