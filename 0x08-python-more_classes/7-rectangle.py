#!/usr/bin/python3
"""declaration"""


class Rectangle:
    """rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """ overrides str method """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.height):
            string += (str(self.print_symbol)) * self.width + '\n'
        return string[:-1]

    def __repr__(self):
        """ overrides repr method """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ says goodbye """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
