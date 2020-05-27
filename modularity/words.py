def fetch_words():
    from urllib.request import urlopen

    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()

        for words in line_words:
            story_words.append(words)

    story.close()

    return story_words


def print_words(story_words):
    for words in story_words:
        print(words)


def main():
    story_words = fetch_words()
    print_words(story_words)


if(__name__ == '__main__'):
    main()
