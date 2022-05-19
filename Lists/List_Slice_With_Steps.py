# List slice with step: [start:end:step]

from re import X


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::1]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letters[::2]) # ['a', 'c', 'e', 'g', 'i']

print(letters[1::2]) # ['b', 'd', 'f', 'h', 'j']
print(letters[2:8:2]) # ['c', 'e', 'g'] [start:end:step]
print(letters[1:20:3]) # ['b', 'e', 'h']



