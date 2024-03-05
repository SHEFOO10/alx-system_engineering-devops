#!/usr/bin/python3
""" 2. Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of
    all hot articles for a given subreddit.
    """
    request_url = "https://www.reddit.com/r/{}/hot.json"\
                  .format(subreddit)
    if (after is not None):
        request_url += "?after={}".format(after)
    res = requests.get(
        url=request_url,
        headers={"User-Agent": "DD/v1.0"}
    )
    if res.status_code == 302 or res.status_code == 404:
        return None
    result = res.json()
    for post in result.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    after = result['data'].get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
