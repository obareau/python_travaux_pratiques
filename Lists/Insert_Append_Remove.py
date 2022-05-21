# insert][].insert

words = ['apple', 'banana', 'cat']
print(words) # ['apple', 'banana', 'cat']

words.insert(2, 'zebra')
print(words) # ['apple', 'banana', 'zebra', 'cat']

words.insert(0, 'dog')
print(words) # ['dog', 'apple', 'banana', 'zebra', 'cat']

# Instead of this, use append (next slide)
words.insert(len(words), 'olifant')
print(words) # ['dog', 'apple', 'banana', 'zebra', 'cat', 'olifant']

# append[].append

names = ['Foo', 'Bar', 'Zorg', 'Bambi']
print(names) # ['Foo', 'Bar', 'Zorg', 'Bambi']

names.append('Qux')
print(names) # ['Foo', 'Bar', 'Zorg', 'Bambi', 'Qux']

# remove[].remove

names = ['Joe', 'Kim', 'Jane', 'Bob', 'Kim']
print(names) # ['Joe', 'Kim', 'Jane', 'Bob', 'Kim']

print(names.remove('Kim')) # None
print(names) # ['Joe', 'Jane', 'Bob', 'Kim']

print(names.remove('George'))
8 # Traceback (most recent call last):
9 # File "examples/lists/remove.py", line 9, in <module>
10 # print(names.remove('George')) # None
11 # ValueError: list.remove(x): x not in list