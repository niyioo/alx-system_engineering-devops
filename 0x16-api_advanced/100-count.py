#!/usr/bin/python3
"""
Recursively queries the Reddit API, parses the title of all hot articles, and
prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively count the occurrences of keywords
    in the titles of hot articles
    for a subreddit and print the results.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): A token to indicate the starting point for pagination.
        count_dict (dict): A dictionary to store the counts of keywords.

    Returns:
        None
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

        # Initialize the count_dict if it's None (only in the first call)
        if count_dict is None:
            count_dict = {}

        for post in posts:
            title = post['data']['title'].lower()
            words = title.split()  # Split title into words
            for word in words:
                # Check if the word is in the word_list and not a variation
                if (
                    word in word_list and
                    not word.endswith('.') and
                    not word.endswith('!') and
                    not word.endswith('_')
                ):
                    # Count the word (case-insensitive) in the count_dict
                    count_dict[word.lower()] = count_dict.get(word.lower(), 0)
                    count_dict[word.lower()] += 1

        # Check if there are more pages (pagination)
        after = data['data']['after']
        if after:
            # Recursively call the function to fetch the next page
            count_words(subreddit, word_list, after, count_dict)
        else:
            # Sort and print the results
            sorted_results = sorted(count_dict.items(),
                                    key=lambda item: (-item[1], item[0]))
            for word, count in sorted_results:
                print(f"{word}: {count}")
    else:
        # Invalid subreddit or other error, print nothing
        return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
