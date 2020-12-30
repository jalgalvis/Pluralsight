#! /usr/bin/env python3
"""Retrieve and print words from a URL"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL

    :param url: The URL of UTF-8 text document.
    :return: A list of strings containing the words from the document
    """

    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    # in case the function is called from a module returns the list
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


# with the following statement we use __name__ to determine if the module
# is called from another module or if it's being called as a script.

if __name__ == '__main__':
    main(sys.argv[1])
