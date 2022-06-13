# coding: utf-8

# Calculate circle's area and circumference

import math 

r = 7
pi = 3.14 # We can use the real Pi with python math library instead
print("The area is : ", r * r * pi)  # 153.86
print("The circumference is :", 2 * r * pi) # 43.96

print("The area is : ", r * r * math.pi)
print("The circumference is :", 2 * r * math.pi)
