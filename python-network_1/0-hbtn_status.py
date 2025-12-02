#!/usr/bin/python3
from urllib import request

url = "https://intranet.hbtn.io/status"
with request.urlopen(url) as response:
    data = response.read()

print(data)
