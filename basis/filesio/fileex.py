from pprint import pprint as pp

myFile = open('text.txt', mode='wt')

myFile.write('What are the roots that clutch, ')
myFile.write('\nwhat branches grow')
myFile.write('\nOut of this stony rubbish?')

# you need to close the file for the content to be visible to others programs!
myFile.close()

sameFile = open('text.txt', mode='at')

sameFile.writelines(
    ['\ntesting', '\nout']
)

sameFile.close()

with open('text.txt', mode='rt') as f:
    pp(f.read())

# close is called at the end