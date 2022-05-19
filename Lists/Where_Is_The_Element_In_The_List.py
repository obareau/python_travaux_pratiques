# words = ['cat', 'dog', 'snake', 'camel']
# print(words.index('snake'))

# print(words.index('python'))

# Traceback (most recent call last):
# File "examples/lists/index.py", line 6, in <module>
# print(words.index('python'))
# ValueError: 'python' is not in list

words = ['cat', 'dog', 'snake', 'camel']

name = 'snake'
if name in words:
    print(words.index(name))

name = 'python'

if name in words:
    print(words.index(name))