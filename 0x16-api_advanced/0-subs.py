#!/usr/bin/python3
"""
Queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit,
        or 0 if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Define the API endpoint URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Invalid subreddit or other error, return 0
        return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
