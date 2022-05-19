# Anything can be a lists
# • Comma separated values
# • In square brackets
# • Can be any value, and a mix of values: Integer, Float, Boolean, None, String, List, Dictionary,
# …
# • But usually they are of the same type:
# • Distances of astronomical objects
# • Chemical Formulas
# • Filenames
# • Names of devices
# • Objects describing attributes of a network device.
# • Actions to do on your data

stuff = [42, 3.14, True, None, "Foo Bar", ['another', 'list'], {'a': 'Dictionary', '\
language' : 'Python'}]
print(stuff)

# Any layout
# • Layout is flexible
# • Trailing comma is optional. It does not disturb us. Nor Python

more_stuff = [
    42,
    3.14,
    True,
    None,
    "Foo Bar",
    ['another', 'list'],
    {
        'a': 'Dictionary',
        'language' : 'Python',
    },
]

print(more_stuff)

