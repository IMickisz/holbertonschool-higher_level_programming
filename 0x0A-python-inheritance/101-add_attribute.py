#!/usr/bin/python3
"""101-add_attribute.py
You are not allowed to import any module.
Function: add_attribute
"""


def add_attribute(obj, objname, value):
    """Function that adds a new attribute to an object if it's possible."""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
