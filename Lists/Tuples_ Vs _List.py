#
# A tuple is a fixed-length immutable list. It cannot change its size or content.
# • A tuple is denoted with parentheses: (1,2,3)
#
# http://docs.python.org/tutorial/datastructures.htmlLists

t = ('a', 'b', 'c')
print(t) # ('a', 'b', 'c')

# List
# • Elements of a list can be changed via their index or via the list slice notation.
# • A list can grow and shrink using append and pop methods or using the slice notation.
# • A list is denoted with square brackets: [1, 2, 3]

l = ['abc', 'def', 'qqrq']
t = tuple(l)
print(l) # ['abc', 'def', 'qqrq']
print(t) # ('abc', 'def', 'qqrq')

l = ['abc', 'def', 'qqrq','abc']
t = tuple(l)
print(l) # ['abc', 'def', 'qqrq', 'abc']
print(t)

# Tuples are rarely used. There are certain places where Python or some module require tuple (instead
# of list) or return a tuple (instead of a list)
# and in each place it will be explained. Otherwise you don’t need to use tuples.
# e.g. keys of dictinoaries can be tuple (but not lists).