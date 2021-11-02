# coding: utf-8

# ! let's guess the number between 1 -20 !

import random

hidden= random.randrange(1, 21)

print("The hidden value is: ", hidden)

user_input = input("Please enter your guess: ")
print(user_input)

guess = int(user_input)

if guess == (hidden):
    print ("Hit !")
    
elif guess < hidden:
    print("Your guess is too low")
else:
    print("Your guess is too high")