# Access single element: [index]
# • Access a sublist: [start:end]
# • Creates a copy of that sublist

import random

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

print(planets) # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

print(len(planets)) # 6

print(planets[0]) # Mercury
print(type(planets[0])) # <class 'str'>
print(planets[3]) # Mars

print(planets[0:1]) # ['Mercury']
print(type(planets[0:1])) # <class 'list'>
print(planets[0:2]) # ['Mercury', 'Venus']
print(planets[1:3]) # ['Venus', 'Earth']

print(planets[2:]) # ['Earth', 'Mars', 'Jupiter', 'Saturn']
print(planets[:3]) # ['Mercury', 'Venus', 'Earth']

print(planets[:]) # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn\']

print(planets[random.randrange(0, 6)]) # not sure about my range ...
