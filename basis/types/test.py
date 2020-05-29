x = [1, 2, 3]
y = [1, 2, 3]

if (x == y):
  print('Variable are equal by value')

if (x is not y):
  print('Variable are not equal by identity')


def flag (message, decor = '-'):
    line = decor * len(message)

    print(line)
    print(message)
    print(line)

flag('France')

toto, tata = ('supertoto', 'supertata')

print(toto, tata)

testString = "jesuisundev".partition('suis')

print(testString)


formatTest = "{0} suis un {1}".format('je', 'dev')
print(formatTest)