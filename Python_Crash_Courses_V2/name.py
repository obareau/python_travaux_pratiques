# Return name with each words capitalized 
name = "ada lovelace"
print(name.title())
# Ada Lovelace

# Some useful methods
name2 = "Ada Lovelace"
print(name2.upper())
print(name2.lower())
# ADA LOVELACE
# ada lovelace

# Using Variables in Strings
gender = "miss"
first_name = "ada"
last_name = "lovelace"
# f is for f-strings
full_name = f"{gender} {first_name} {last_name}"
print(f"\tHello, \n\t{full_name.title()}!")

# Stripping Whitespace
favorite_language = " python "
print (favorite_language.rstrip())
print (favorite_language.lstrip())

