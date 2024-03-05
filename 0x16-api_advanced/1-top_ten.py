#!/usr/bin/python3
""" the titles of the first 10 hot posts listed for a given subreddit. """
import requests


def top_ten(subreddit):
    """ Get top 10 subreddits """
    res = requests.get(
        url='https://www.reddit.com/r/{}/hot.json?limit=9'.format(subreddit),
        headers={"User-Agent": "DD/v1.0"},
        allow_redirects=False
    )
    if res.status_code == 302 or res.status_code == 404:
        print(None)
        return
    results = res.json()
    hot_posts = results.get('data').get('children')
    for post in hot_posts:
        print(post.get('data').get('title'))
