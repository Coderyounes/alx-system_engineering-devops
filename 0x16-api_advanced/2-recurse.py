#!/usr/bin/python3
""" DOC DOC DOC"""

from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """ DOC DOC DOC"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:uhXwbQac5CHtsASxHSxtjQ:1.0.0\
            (by /u/Dizzy_Back7390)"}
    param = {'after': after}

    response = get(url, headers=headers, params=param)
    if response.status_code == 200:
        req_j = response.json()
        data = req_j.get("data").get("children")
        for post in data:
            title = post.get("data").get("title")
            hot_list.append(title)
        after = req_j.get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
