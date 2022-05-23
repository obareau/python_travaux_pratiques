filename = "Tp_Files/examples/files/numbers.txt" # Relative Path

with open(filename, 'r') as fh:

    lines_str = fh.read()
# reads all the lines into a string

print(len(lines_str))
# number of characters in file

print(lines_str)
# the content of the file