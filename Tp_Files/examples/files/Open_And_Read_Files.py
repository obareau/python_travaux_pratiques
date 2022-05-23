filename = "examples/files/number.txt"

with open(filename, 'r') as fh:
    for line in fh:
        print(line)
        