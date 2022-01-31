#!/usr/bin/python3
"""100-my_int.py
The class MyInt is a rebel. MyInt has == and != operators inverted.
You are not allowed to import any module.
"""


class MyInt(int):
    """class that inherits from int"""

    """__init__ method that is called when a new instnace is created."""
    def __init__(self, my_int):
        self.my_int = my_int

    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
