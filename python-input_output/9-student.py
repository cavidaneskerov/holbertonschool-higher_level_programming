#!/usr/bin/python3
"""Write a class and change it to JSON data"""
import json


class Student:
"""Student class for json"""

    def __init__(self, first_name, last_name, age):
        """def for atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """To json function"""
        return Student.__dict__
