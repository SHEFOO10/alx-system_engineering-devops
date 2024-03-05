#!/usr/bin/python3
""" Get subscribers of subreddit"""
import requests


def number_of_subscribers(subreddit):
    """
        Get subscribers of subreddit
    """
    headers = {'User-Agent': 'Chrome/111.0.0.0 Safari/537.36'}

    res = requests.get(
        url="https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers=headers,
        allow_redirects=False)
    if (res.status_code == 404 or res.status_code == 302):
        return 0
    return res.json().get('data').get('subscribers')
