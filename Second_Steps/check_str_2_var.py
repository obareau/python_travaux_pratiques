# coding: utf-8

# ! for later use !
# use regexes to verify that the str looks like a numbers
# wrap the code in try-block to catch any exception raised during conversion

val = input("Type a number: ")

print(val)
print(val.isdecimal())
print(val.isnumeric())
print(val.isalpha())
print(val.isupper())
print(val.isspace())

if val.isdecimal():
    num = int(val)
    print(num)