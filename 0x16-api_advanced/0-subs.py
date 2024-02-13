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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-agent': "linux.ALX-Tasks:v1.0.0 (by /u/Dizzy_Back7390)"}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 404:
        r_json = response.json()
        data = r_json.get('data')
        subs = data.get('subscribers')
        return subs
    return 0
