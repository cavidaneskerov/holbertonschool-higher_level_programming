#!/usr/bin/python3
"""Appending word to text"""


def append_write(filename="", text=""):
    """Apeendgin word to text"""
    with open(filename, "w") as f:
        return f.write(text)
  
