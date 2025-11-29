#!/usr/bin/python3
"""Write a class and change it to JSON data"""


class Student:
    """Student class for json"""

    def __init__(self, first_name, last_name, age):
        """def for atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To json function"""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

