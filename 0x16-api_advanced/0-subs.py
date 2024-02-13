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
    user_agent = {
        "User-Agent": "My-User-Agent"
        }

    response = requests.get(url, headers=user_agent)
    all_data = response.json()

    try:
        return all_data.get('data').get('subscribers')

    except:
        return 0
