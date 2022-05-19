# In this example we use a list of lists that we have not learned yet, but don’t worry about that for
# now.
# Focus on the output of the two print statements.

data = [
    ["Foo Bar", 42, "good"],
    ["Bjorg", 12345, "bad"],
    ["Roza", 7, "ugly"],
    ["Long Name Joe", 3, "evil"],
    ["Joe", 12345677889, "kid"],
]

def print_lines(text):
    print('-' * text)

for entry in data:
    print("{} {}".format(entry[0], entry[1]))


print_lines(38)

for entry in data:
    print("{:<16}|{:>12}|{:^12}".format(entry[0], entry[1], entry[2]))

print_lines(38)

txt = "Some text"

print("'{}'".format(txt)) # as is: 'Some text'
print("'{:12}'".format(txt)) # left: 'Some text '
print("'{:<12}'".format(txt)) # left: 'Some text '
print("'{:>12}'".format(txt)) # right: ' Some text'
print("'{:^12}'".format(txt)) # center: ' Some text '