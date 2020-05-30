def gen123():
    yield 1
    yield 2
    yield 3

def gen426():
    """[summary]

    Yields:
        [type] -- [description]
    """
    print("About to 2")
    yield 2

    print("About to 4")
    yield 4

    print("About to 6")
    yield 6

    print("About to return")

generatorTest = gen123()

print(next(generatorTest))
print(next(generatorTest))
print(next(generatorTest))

generatorToto = gen426()

for stuff in gen426():
  print(stuff)