#!/usr/bin/python3
"""
Fetches a URL and displays the body (utf-8 decoded).
Handles HTTP errors and prints the status code.
"""
import requests
import sys

if "__name__" == "__main__":
    url = sys.argv[1]
    url = sys.argv[2]

    data = {"email": email}
    r = requests.post(
        url,
        data=data,
    )
    print(r.text)
