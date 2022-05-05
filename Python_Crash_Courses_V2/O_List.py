bicycles = ['vélo-pliant', 'ruffian', 'canondale','motobécane', 'truc rouillé']

message = f"Bibi va s'acheter un {bicycles[0].title()}"
print (message)

# return : Bibi va s'acheter un Vélo-Pliant

bicycles[0] = 'que dalle'
print (message) # Just a test

message = f"Bibi va s'acheter un {bicycles[0].title()}"
print (message) # ATTENTION need to do it again to reflect change in list

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() Method
# Sometimes you’ll want to use the value of an item after you remove it from a
# list. For example, you might want to get the x and y position of an alien that
# was just shot down, so you can draw an explosion at that position. In a web
# application, you might want to remove a user from a list of active members
# and then add that user to a list of inactive members.
# The pop() method removes the last item in a list, but it lets you work
# with that item after removing it. The term pop comes from thinking of a
# list as a stack of items and popping one item off the top of the stack. In
# this analogy, the top of a stack corresponds to the end of a list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# We start by defining and printing the list motorcycles at u. At v we pop
# a value from the list and store that value in the variable popped_motorcycle.
# We print the list at w to show that a value has been removed from the list.
# Then we print the popped value at x to prove that we still have access to
# the value that was removed.
# The output shows that the value 'suzuki' was removed from the end of
# the list and is now assigned to the variable popped_motorcycle:

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping Items from any Position in a List
# You can use pop() to remove an item from any position in a list by including
# the index of the item you want to remove in parentheses.

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an Item by Value
# Sometimes you won’t know the position of the value you want to remove
# from a list. If you only know the value of the item you want to remove, you
# can use the remove() method.
# For example, let’s say we want to remove the value 'ducati' from the list of
# motorcycles.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that’s being
# removed from a list. Let’s remove the value 'ducati' and print a reason for
# removing it from the list:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Stopped at page 43 of Python Crash Course V2