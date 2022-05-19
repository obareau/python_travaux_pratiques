x = 0b101010


print("{:b}".format(x)) # binary: 101010
print("{:c}".format(x)) # character: *
print("{:d}".format(x)) # decimal: 42 (default)
print("{:o}".format(x)) # octal: 52
print("{:x}".format(x)) # hexa: 2a
print("{:X}".format(x)) # hexa: 2A
print("{:n}".format(x)) # number: 42


print("{}".format(x)) # defaults to decimal

x = 412.345678901

print("{:e}".format(x)) # exponent: 4.123457e+02
print("{:E}".format(x)) # Exponent: 4.123457E+02
print("{:f}".format(x)) # fixed point: 412.345679 (default precision is 6)
print("{:.2f}".format(x)) # fixed point: 412.35 (set precision to 2)
print("{:F}".format(x)) # same as f. 412.345679
print("{:g}".format(x)) # generic: 412.346 (default precision is 6)
print("{:G}".format(x)) # generic: 412.346
print("{:n}".format(x)) # number: 4412.346
print("{}".format(x)) # defaults to g 412.3456789