# coding: utf-8
# The SALADOTRON
# let's compose a nice fuits salad choose between fruits and a number of ingredient 2 to 6

import random

fruits = [ "Apple", "Pear", "Banana", "Peach", "Orange", "Mango", "Durian", "Papaya", "Watermelon", "Strawberry", "Raspberry", "Kiwi", "Blackcurrant"]
print("List of ingredients: \n")
for fruit in  fruits:
    print (fruit)
print()

n_ingredient = random.randrange(2, 7) # 2 to 6 cause 7 is not included
salad = random.sample(fruits, n_ingredient)
print ("Here is the recipe:",  salad)
