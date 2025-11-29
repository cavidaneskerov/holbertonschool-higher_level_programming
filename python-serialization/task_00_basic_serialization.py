#!/usr/bin/python3
"""Serialization project first"""
import json

def serialize_and_save_to_file(data, filename):
    """serialize and save to file"""
    with open(filename, "w") as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    """load and deserialization file"""
    with open(filename, "r") as s:
        return json.load(s)
