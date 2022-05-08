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

# It’s important to realize that this is, in a real sense, an illusion: you’re simply rounding the display of the true machine value.

# One illusion may beget another. For example, since 0.1 is not exactly 1/10, summing three values of 0.1 may not yield exactly 0.3, either:
print (.1 + .1 + .1 == .3)

# Also, since the 0.1 cannot get any closer to the exact value of 1/10 and 0.3 cannot get any closer to the exact value of 3/10, then pre-rounding with round() function cannot help:
print (round(.1, 1) + round(.1, 1) + round(.1, 1)) == round(.3, 1)

# Though the numbers cannot be made closer to their intended exact values, the round() function can be useful for post-rounding so that results with inexact values become comparable to one another:

print (round(.1 + .1 + .1, 10)) == round(.3, 10)

# Representation Error¶
# This section explains the “0.1” example in detail, and shows how you can perform an exact analysis of cases like this yourself. Basic familiarity with binary floating-point representation is assumed.

# Representation error refers to the fact that some (most, actually) decimal fractions cannot be represented exactly as binary (base 2) fractions. This is the chief reason why Python (or Perl, C, C++, Java, Fortran, and many others) often won’t display the exact decimal number you expect.

# Why is that? 1/10 is not exactly representable as a binary fraction. Almost all machines today (November 2000) use IEEE-754 floating point arithmetic, and almost all platforms map Python floats to IEEE-754 “double precision”. 754 doubles contain 53 bits of precision, so on input the computer strives to convert 0.1 to the closest fraction it can of the form J/2**N where J is an integer containing exactly 53 bits.