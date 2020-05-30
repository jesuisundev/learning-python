words = "Hello darkness my old friend".split()

print(words)

# comprehension list
compList = [len(word) for word in words]
print(compList)

compSet = {len(word) for word in words}
print(compSet)


# dict comprehension list

countryToCapital = {
  "France": "Paris",
  "Spain": "Madrid",
  "England": "London"
}

capital_to_country = {capital: country for country, capital in countryToCapital.items() if country is not "England"}
print(capital_to_country)

# iteration protocol
def first(iterable):
    # get iterator built-in
    iterator = iter(iterable)

    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

toto = first(capital_to_country)

print(toto)