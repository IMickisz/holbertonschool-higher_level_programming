#!/usr/bin/python3
"""
Module with the class Rectangle that define a rectangle
"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        The instance method called when a new object is created.
        Args:
            - width (int):
                . the width of a rectangle
                . must be an int
                . if width is less than 0, raise ValueError
            - height (int):
                . the height of a rectangle
                . must be an integer
                . if height is less than 0, raise ValueError
        Attribute:
            - __width: the width is a private attribute
            - __height: the height is a private attribute
        """
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """This method retrieve the data of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method set the data of the width
        Args:
            - value (int): the width of the rectangle
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method retrieve the data of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This method set the data of the height.
        Args:
            - value (int): the height of the rectangle
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = (self.__height + self.width) * 2
        return perimeter

    def __str__(self):
        """returns an 'informal' and nicely printable string representation
of an instance"""
        print_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return print_rectangle
        else:
            for row in range(self.__height):
                for column in range(self.__width):
                    print_rectangle += '#'
                if row < self.__height - 1:
                    print_rectangle += '\n'
            return print_rectangle

    def __repr__(self):
        """returns an ???official??? string representation of an instance"""
        w = self.__width
        h = self.__height
        return "Rectangle({:d}, {:d})".format(w, h)

    def __del__(self):
        """instance method called when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
