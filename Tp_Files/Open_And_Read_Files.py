filename = "Tp_Files/examples/files/numbers.txt" # Relative Path

with open(filename, 'r') as fh:
    for line in fh:
        print(line)
        