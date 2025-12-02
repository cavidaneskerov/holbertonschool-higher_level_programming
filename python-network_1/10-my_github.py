#!/usr/bin/python3
""" jhsdhfjsdhf jhfjhh hdjfh jf"""
import requests
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(name, password))

    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)

    print(data.get("id"))
