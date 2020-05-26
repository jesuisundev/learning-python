from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_worlds = []
numberOfChar = 0

for line in story:
    decodedLine = line.decode()
    numberOfChar += len(decodedLine)

print("There are %s characters in this story" % numberOfChar)

story.close()