import json

with open('input.json', 'r') as input:
  obj = json.load(input)
  print('Hello, ' + obj['name'])