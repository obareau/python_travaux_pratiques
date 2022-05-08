# coding: utf-8

# Let's play with datatypes

print (type(23))            # int
print (type(3.14))          # float
print (type('hello world')) # str

print (type("23"))          # str
print (type("3.24"))        # str

print (type(None))          # NoneType
print (type(True))          # bool
print (type(False))         # bool

print (type([]))            # list
print (type(()))            # tuple
print (type({}))            # dict

# print (type(hello))

# Strings must be enclosed in quotes.
# Numbers must be NOT enclosed in quotes.

# Values type in Numpy
# Numpy but also others languages might have them

# int8
# int32
# float32
# float64
# ... TBC 

# Floating Point Arithmetic: Issues and Limitations
print(0.1)
print(0.2)
print (0.1 + 0.2)
# In the same way, no matter how many base 2 digits you’re willing to use, the decimal value 0.1 cannot be represented exactly as a base 2 fraction. In base 2, 1/10 is the infinitely repeating fraction

# 0.0001100110011001100110011001100110011001100110011...
# https://docs.python.org/3/tutorial/floatingpoint.html

# Stop at any finite number of bits, and you get an approximation. On most machines today, floats are approximated using a binary fraction with the numerator using the first 53 bits starting with the most significant bit and with the denominator as a power of two. In the case of 1/10, the binary fraction is 3602879701896397 / 2 ** 55 which is close to but not exactly equal to the true value of 1/10.

# Many users are not aware of the approximation because of the way values are displayed. Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine. On most machines, if Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display