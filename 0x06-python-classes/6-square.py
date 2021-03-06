#!/usr/bin/python3
"""6-square.py

Write a class Square that defines a square by:

- Private instance attribute: size
property def size(self): to retrieve it
property setter def size(self, value): to set it:
> size must be an integer, otherwise raise a TypeError exception with the
messagesize must be an integer
> if size is less than 0, raise a ValueError exception with the message size
must be >= 0

- Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
> position must be a tuple of 2 positive integers, otherwise raise a TypeError
exception with the message position must be a tuple of 2 positive integers

- Instantiation with optional size and optional position: def __init__(self,
size=0, position=(0, 0)):

- Public instance method: def area(self): that returns the current square area

- Public instance method: def my_print(self): that prints in stdout the square
with the character #:
if size is equal to 0, print an empty line
"""


class Square:
    """class that defines a square"""
    """The __init__ method is run as soon as the object class is instantiated.

    Args:
    size: The size of the square.
    position: coordonné in the square (composed of two interger)

    Attribute:
    __size: (Private instance attribute) size of the square.
    __position: (Private instance attribute) position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.position = position
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size corresponding to the parameters"""
        self.__size = value
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

    @property
    def position(self):
        """Return the position of the # in the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of position corresponding to the parameters"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This method print in stdout the square made of #"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            print("")
        for row in range(self.__size):
            for pos in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            print("")
