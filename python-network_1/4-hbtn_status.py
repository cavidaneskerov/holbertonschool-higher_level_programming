#!/usr/bin/python3
"""
Fetches a URL and displays the body (utf-8 decoded).
Handles HTTP errors and prints the status code.
"""
import requests

r = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print("-type:", type(r.text))
print("-content:", r.text )
