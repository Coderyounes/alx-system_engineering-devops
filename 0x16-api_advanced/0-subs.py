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
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'chalwe_demo_reddit_module'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if not response.status_code == 200:
        return 0
    subscribers = response.json().get('data').get('subscribers')
    if subscribers is not None:
        return subscribers
    return 0
