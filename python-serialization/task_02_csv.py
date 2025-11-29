#!/usr/bin/python3
"""CSV to JSON with pickle"""
import csv, json


def convert_csv_to_json(csv_filename):
    """Read CSV file and write JSON data to data.json"""
    try:
        data_list = []
        with open(csv_filename, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)
            return True
    except Exception as e:
        return False
