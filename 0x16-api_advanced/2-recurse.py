#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetch hot articles for a subreddit
    and store their titles in a list.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the article titles.
        after (str): A token to indicate the starting point for pagination.

    Returns:
        list: A list of article titles, or None if no results are found.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Define the API endpoint URL for hot posts in the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    # If 'after' token is provided, add it to the URL to fetch the next page
    if after:
        url += f'&after={after}'

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the titles of hot posts
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there are more pages (pagination)
        after = data['data']['after']
        if after:
            # Recursively call the function to fetch the next page
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        # Invalid subreddit or other error, return None
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
