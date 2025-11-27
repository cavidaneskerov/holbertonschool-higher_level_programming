#!/usr/bin/python3
"""This defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle with # characters"""
        if self.width == 0 or self.height == 0:
            return ""
        l = (f"{self.print_symbol}" * self.width for _ in range(self.height))
        return "\n".join(l)

    def __repr__(self):
        """Return the rectangle repr"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
