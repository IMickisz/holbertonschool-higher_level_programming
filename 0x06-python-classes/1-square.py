#!/usr/bin/python3
"""0-square.py

Write a class Square that defines a square by:
- Private instance attribute: size
- Instantiation with size (no type/value verification)
"""


class Square:
    """class that defines a square"""
    """The __init__ method is run as soon as the object class is instantiated.

    Args:
    size: The size of the square.

    Attribute:
    __size: (Private instance attribute) size of the square.
    """
    def __init__(self, size):
        self.__size = size
