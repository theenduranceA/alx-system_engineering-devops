#!/usr/bin/python3
""" Module for Reddit API."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Function that queries the Reddit API and
    returns a list containing the titles of all hot articles."""

    params = {}
    if after is not None:
        params = {"after": after}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Endurance Aneke"}
    response = requests.get(url, headers=headers, params=params)

    try:
        _after = response.json().get("data").get("after")
        for _ in response.json().get("data").get("children"):
            hot_list.append(_.get("data").get("title"))
        if _data is not None:
            return(recurse(subreddit, _after, hot_list=[]))
        else:
            return(hot_list)

    except Exception:
        return(None)
