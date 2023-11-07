#!/usr/bin/python3
""" Module for Reddit API."""

import sys
import requests


def count_words(subreddit, word_list=[], count_list=[], after=None):
    """ Function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces."""

    param = {}
    _after = None
    if after is not None:
        param = {"after": after}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Endurance Aneke"}
    response = requests.get(url, headers=headers, params=param)

    try:
        _after = response.json().get("data").get("after")
        for _ in response.json().get("data").get("children"):
            count_list.append(_.get("data").get("title"))
    except Exception:
        return(None)
        if _after is not None:
            return(count_words(subreddit, word_list, count_list, _after))
        else:
            my_word = dict.fromkeys((word_list.lower()), 0)
            _new = ""
            for _list in count_list:
                _new = _list.lower()
                for _word in word_list:
                    if _word in _new:
                        my_word[_word] += 1
            for key in my_word:
                print("{:s}: {:d}".format(key, my_word[key]))
            return(count_list)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("I gave in my best at this subreddit API Project.")
    else:
        print(len(count_words(sys.argv[1], [x for x in sys.argv[2].split()])))
