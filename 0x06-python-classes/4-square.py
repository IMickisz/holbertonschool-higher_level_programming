#!/usr/bin/python3
"""4-square.py

Write a class Square that defines a square by:

- Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:
> size must be an integer, otherwise raise a TypeError exception with the
messagesize must be an integer
> if size is less than 0, raise a ValueError exception with the message size
must be >= 0

- Public instance method: def area(self): that returns the current square area
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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2
