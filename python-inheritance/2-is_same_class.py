#!/usr/bin/python3
"""Python inheritance with same object"""


def is_same_class(obj, a_class):
    """Inheritance with same classes"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
