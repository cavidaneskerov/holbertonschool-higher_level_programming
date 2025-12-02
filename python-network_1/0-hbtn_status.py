#!/usr/bin/python3
from urllib import request

url = "https://intranet.hbtn.io/status"
response = request.urlopen(url)

data = response.read()
print(data)
