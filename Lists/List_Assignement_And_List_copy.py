x = ['apple', 'bob', 'cat', 'drone']
y = x
x[0] = 'qqrq'
print(x) # ['qqrq', 'bob', 'cat', 'drone']
print(y) # ['qqrq', 'bob', 'cat', 'drone']
# • There is one list in the memory and two pointers to it.
# • If you really want to make a copy the pythonic way is to use the slice syntax.
# • It creates a shallow copy

from copy import deepcopy

x = ['apple', 'bob', 'cat', 'drone']
y = deepcopy(x)

x[0] = 'qqrq'

print(x) # ['qqrq', 'bob', 'cat', 'drone']
print(y) # ['apple', 'bob', 'cat', 'drone']