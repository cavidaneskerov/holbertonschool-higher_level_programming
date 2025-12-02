#!/usr/bin/python3
from urllib import request

url = "https://intranet.hbtn.io/status"
with request.urlopen(url) as response:
    data = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode("utf-8")))
