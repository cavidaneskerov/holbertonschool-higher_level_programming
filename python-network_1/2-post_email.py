#!/usr/bin/python3
"""
Fetches and displays the X-Request-Id header from a given URL.
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("utf-8")
    req = request.Request(url, data=data, methods="POST")

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
