age = 42.12 # float
name = "Foo Bar" # string

str_concatenate = "The user " + name + ' was born ' + str(age) + " years ago."
print(str_concatenate)

str_percentage = "The user %s was born %s years ago." % (name, age) # I like this syntax !
print(str_percentage)

str_format = "The user {} was born {} years ago.".format(name, age) # with format method
print(str_format)

str_f_string = f"The user {name} was born {age} years ago." # python > V3.6 only
print(str_f_string)
