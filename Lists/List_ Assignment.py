# List assignment works in “parallel” in Python.

x, y = 1, 2
print(x) # 1
print(y) # 2

x, y = y, x
print(x) # 2
print(y) # 1
x,y = f() # works if f returns a list of 2 elements

# It will throw a run-time ValueError exception if the number
# of values in the returned list is not 2. (Both for fewer and for more return values)