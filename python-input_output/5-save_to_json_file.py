#!/usr/bin/python3
"""Json obj write to file"""
import json


def save_to_json_file(my_obj, filename):
    """Json obj write to file"""
    with open(filename, "w") as s:
        return s.dump(my_obj, f)
