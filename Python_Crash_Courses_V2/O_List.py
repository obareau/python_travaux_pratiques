bicycles = ['vélo-pliant', 'ruffian', 'canondale','motobécane', 'truc rouillé']

message = f"Bibi va s'acheter un {bicycles[0].title()}"
print (message)

# return : Bibi va s'acheter un Vélo-Pliant

bicycles[0] = 'que dalle'
print (message) # Just a test

message = f"Bibi va s'acheter un {bicycles[0].title()}"
print (message) # need to do it again to reflect change in list
