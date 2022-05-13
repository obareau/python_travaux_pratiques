# In Python strings are “immutable”, meaning you cannot change them. You can replace a whole string
# in a variable,
# but you cannot change it.
# In the following example we wanted to replace the 3rd character (index 2), and put “Y” in place. This
# raised an exception

text = "abcd"
print(text) # abcd

# text[2] = "Y" # Doesn't work


print(text)

# HOW TO CHANGE A STRING

text = text[:2] + "Y" + text[3:]
print(text)
print("done!")