#!/usr/bin/python3
"""2-square.py

Write a class Square that defines a square by:

- Private instance attribute: size

- Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message
size must be an integer
if size is less than 0, raise a ValueError exception with the message size must
be >= 0
"""


class Square:
    """class that defines a square"""
    """The __init__ method is run as soon as the object class is instantiated.

    Args:
    size: The size of the square.

    Attribute:
    __size: (Private instance attribute) size of the square.
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
