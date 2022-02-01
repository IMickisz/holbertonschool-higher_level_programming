#!/usr/bin/python3
"""9-student.py
Module that defines a class Student.
You are not allowed to import any module.
"""


class Student:
    """Class that defines a student."""

    """The __init__ method is called when a new instnace is created."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation
        of a Student instance.
        """
        return self.__dict__
