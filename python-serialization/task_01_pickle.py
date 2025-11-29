#!/usr/bin/python3
"""Python serialization with pickle"""
import pickle


class CustomObject:
    """CustomObject class for example"""

    def __init__(self, name, age, is_student):
        """Initialization this atributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display all atributes"""
        print(f"Name: {self.age} \n Age: {self.age} \n Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize this object and save it to a file"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a file"""
        with open(filename, "rb") as f:
            return pickle.load(f)
