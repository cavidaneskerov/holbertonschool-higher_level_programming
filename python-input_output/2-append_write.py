#!/usr/bin/python3
"""Appending word to text"""


def append_write(filename="", text=""):
    """Apeendgin word to text"""
    with open(filename, "a") as f:
        return f.write(text)
  
