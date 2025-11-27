#!/usr/bin/python3
"""This defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value_1):
        if not isinstance(value_1, int):
            raise TypeError("width must be an integer")
        if value_1 < 0:
            raise ValueError("width must be >= 0")
        self.__width = value_1
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value_2):
        if not isinstance(value_2, int):
            raise TypeError("height must be an integer")
        if value_2 < 0:
            raise ValueError("height must be >= 0")
        self.__width = value_2

    def area(self):
      return self.width * self.height
    def perimeter(self):
      if self.width == 0 or self.height == 0:
          return 0
      else:
          return (self.width + self.height) * 2
