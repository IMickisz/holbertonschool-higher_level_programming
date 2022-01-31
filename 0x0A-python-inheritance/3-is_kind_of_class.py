#!/usr/bin/python3
"""3-is_kind_of_class.py
You are not allowed to import any module.
Function: is_same_class.
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    """
    return isinstance(obj, a_class)
