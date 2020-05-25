import json

def openAndReadInput():
  with open('input.json', 'r') as input:
    obj = json.load(input)
    print('Hello, ' + obj['name'])

def openAndCopyInputToOuput():
  with open('input.json', 'r') as input:
    obj = json.load(input)
    
    with open('output.txt', 'w') as output:
      output.write(obj['name'] + ' : Hoobies\n')
      for hobby in obj['hobbies']:
        output.write(hobby + '\n')

openAndReadInput()
openAndCopyInputToOuput()