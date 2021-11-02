# coding: utf-8

# let's compose a nice fuits salad

import random

fruits = [ "Apple", "Pear", "Banana", "Peach", "Orange", "Mango", "Durian", "Papaya", "Watermelon", "Strawberry", "Raspberry"]
n_ingredient = random.randrange(2, 6)
salad = random.sample(fruits, n_ingredient)
print ("Here is the recipe:",  salad)
