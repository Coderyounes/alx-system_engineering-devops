#!/usr/bin/python3
""" DOC DOC DOC"""

import requests


def top_ten(subreddit):
    """
        top_ten - function return hot post titles
        return - the title or None if fail
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:uhXwbQac5CHtsASxHSxtjQ:1.0.0\
            (by /u/Dizzy_Back7390)"}
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        try:
            results = response.json().get("data")
            if results:
                for post in results["children"]:
                    print(post["data"]["title"])
        except Exception as e:
            print("None")
    else:
        print("None")
