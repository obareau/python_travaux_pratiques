filename = "Tp_Files/examples/files/numbers.txt" # Relative Path

with open(filename, 'r') as fh:

    lines_list = fh.readlines()
# reads all the lines into a list


# print number of lines
print(len(lines_list))

for line in lines_list:
    print(line, end="")
    
# Read all the characters into a string (slurp)

