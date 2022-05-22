planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

for idx, planet in enumerate(planets):
    print(idx, planet)

print('')
enu = enumerate(planet)
print(enu.__class__.__name__)
print(enu)

# 0 Mercury
# 1 Venus
# 2 Earth
# 3 Mars
# 4 Jupiter
# 5 Saturn

enumerate
# <enumerate object at 0x7f2c2402adc8>