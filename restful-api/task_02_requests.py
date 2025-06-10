#!/usr/bin/python3
"""
Module to fetch and display or save posts from JSONPlaceholder
"""

import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        with open(
            "posts.csv", "w", newline='', encoding="utf-8"
        ) as csvfile:
            writer = c
