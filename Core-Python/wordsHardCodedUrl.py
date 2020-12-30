from urllib.request import urlopen


def fetch_words_HCU():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    # in case the function is called from a module returns the list
    return story_words


def print_items_HCU(items):
    for item in items:
        print(item)


def main():
    words = fetch_words_HCU()
    print_items_HCU(words)


# with the following statement we use __name__ to determine if the module
# is called from another module or if it's being called as a script.
if __name__ == '__main__':
    main()
