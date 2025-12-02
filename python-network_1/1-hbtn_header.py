#!/usr/bin/python3
"""
Fetches and displays the X-Request-Id header from a given URL.
"""
from urllib import request
import sys
if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        headers = response.info()
        header = headers.get("X-Request-Id")
        print(header)
