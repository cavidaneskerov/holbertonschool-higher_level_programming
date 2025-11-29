#!/usr/bin/python3
"""Python classes for writing file"""


def write_file(filename="", text=""):
    """Function for reading"""
    with open(filename, "w") as f:
        f.write(text)
        print(len(text))
        f.close()
