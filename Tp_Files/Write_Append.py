

# ! Write
with open(filename, 'w') as out: 

    out.write('text\n')
    

# ! Append


filename = "Tp_Files/examples/files/numbers.txt" # Relative Path

with open(filename, 'a') as out:

out.write('append more text\n')