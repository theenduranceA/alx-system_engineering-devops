#!/usr/bin/python3
""" Module for Reddit API."""

import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and
    returns the number of subscribers."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Endurance Aneke"}
    response = requests.get(url, headers=headers)
    try:
        return(response.json().get('data').get('subscribers'))
    except Exception:
        return(0)
