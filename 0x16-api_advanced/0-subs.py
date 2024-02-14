#!/usr/bin/python3
""" Python Script return the number of subscribers """


import requests


def number_of_subscribers(subreddit):
    """
        number_of_subscribers Function Scrap Subscribers Number
            subrredit - channel to check subscribers number
            return - subscribers number
            return - 0 if subreddit not found
    """
    session = requests.Session()
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/121.0.0.0 Safari/537.36"}
    session.headers.update(headers)
    response = session.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
