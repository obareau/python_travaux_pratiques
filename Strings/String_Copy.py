text = "abcd"
print(text) # abcd

text = text + "ef"
print(text) # abcdef

other = text
print(other) # abcdef
text = "xyz"
print(text) # xyz
print(other) # abcdef

# When assigning a variable pointing a string, the new variable is pointing to the same string..
# If we then assign some other string to either of the variables, then they will point to two different
# strings.