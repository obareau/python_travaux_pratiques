fields = ["one", "two", "three", "four", "five", "six"]

together = ":".join(fields)
print(together) # one:two:three:four:five:six

together = ':'.join(fields)
print(together) # one:two and three:four:five:six

mixed = ' -=<> '.join(fields)
print(mixed) # one -=<> two and three -=<> four -=<> five -=<> six

another = ''.join(fields)
print(another) # onetwo and threefourfivesix
