animals = ['chicken', 'cow', 'snail', 'elephant']
print(animals) # ['chicken', 'cow', 'snail', 'elephant']

s = sorted(animals)
print(s) # ['chicken', 'cow', 'elephant', 'snail']
print(animals) # ['chicken', 'cow', 'snail', 'elephant']

r = sorted(animals, reverse=True, key=len)
print(r) # ['elephant', 'chicken', 'snail', 'cow']
print(animals) # ['chicken', 'cow', 'snail', 'elephant']Lists 114

# sort vs. sorted
# The sort() method will sort a list in-place and return None.
# The built-in sorted() function will return the sorted list and leave the original list intact.
# key sort with sorted
# To sort the list according to length using sorted

animals = ['snail', 'cow', 'elephant', 'chicken']
animals_in_abc = sorted(animals)
print(animals)
print(animals_in_abc)

animals_by_length = sorted(animals, key=len)
print(animals_by_length)
['snail', 'cow', 'elephant', 'chicken']
['chicken', 'cow', 'elephant', 'snail']
['cow', 'snail', 'chicken', 'elephant']

# Sorting characters of a string

letters = 'axzb'
print(letters) # 'axzb'
s = sorted(letters)
print(s) # ['a', 'b', 'x', 'z']
print(letters) # 'axzb'

r = ''.join(sorted(letters))
print(r) # abxz