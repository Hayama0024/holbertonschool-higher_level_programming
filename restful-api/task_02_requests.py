#!/usr/bin/python3
"""
Module containing functions for fetching
and printing or saving posts from JSONPlaceholder.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print their titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        with open("posts.csv", "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            for post in data:
                writer.writerow({
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]
                })
