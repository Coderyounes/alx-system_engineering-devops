#!/usr/bin/python3
""" DOC DOC DOC"""

import requests


def top_ten(subreddit):
    """
        top_ten - function return hot post titles
        return - the title or None if fail
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:uhXwbQac5CHtsASxHSxtjQ:1.0.0\
            (by /u/Dizzy_Back7390)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
