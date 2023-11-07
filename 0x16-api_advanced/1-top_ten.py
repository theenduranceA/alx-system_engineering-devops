#!/usr/bin/python3
""" Module for Reddit API."""

import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed."""

    params = {"limit": 10}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Endurance Aneke"}
    response = requests.get(url, headers=headers, params=params)

    try:
        _data = response.json().get("data").get("children")

        for _ in _data:
            print(_.get("data").get("title"))

    except Exception:
        print("None")
