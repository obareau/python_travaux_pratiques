# coding: utf-8
import random

# random.seed(37)
x = random.random()
print(x)


letters = ("azertyuiopqsdfghjklmwxcvbn")
print(random.choice(letters))

os = ["Linux", "OSX", "Win10", "Win11", "BSD"]
print(random.choice(os))

# Rolling dice 
print( 1 + int(6 * random.random()) ) 

# another way 
print(random.randrange(1, 7))
