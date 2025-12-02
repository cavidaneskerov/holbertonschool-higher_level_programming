#!/usr/bin/python3
"""dfjsdfdshfjsdhfj skjsd """
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
def fetch_and_print_posts():
    """Fetch and print posts"""
    r = requests.get(url)
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for post in data:
            print(post.get("title"))

def fetch_and_save_posts():
    """Fetch and save posts"""
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        list = []
        for post in data:
            list.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerow(list)
