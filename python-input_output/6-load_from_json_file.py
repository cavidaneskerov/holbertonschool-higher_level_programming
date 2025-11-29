#!/usr/bin/python3
"""From file object to json"""
import json


def load_from_json_file(filename):
    """From file object to json"""
    with open(filename, "r") as f:
        return json.load(f)
