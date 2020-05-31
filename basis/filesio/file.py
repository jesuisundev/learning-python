import sys

f = open(sys.argv[1], mode='rt')

for line in f:
    print(line)

f.close()