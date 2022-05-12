x = 23

if x:
    print("23 is true")

y = 23
if y:
    print("23 is true")
else:
    print("0 is false")
    
y = 0 #  ! 0 is Always false in python
if y:
    print("0 is true")
else:
    print("0 is false")
    
# ! True and False values in Python
# • None
# • 0
# • ”” (empty string)
# • False
# • [] list
# • {} dictionary
# • () tuple

# ! EVERYTHING ELSE IS TRUE

values = [None, 0, "", False, [], (), {}, "0", True]
for v in values:
    if v:
        print("True value: ",v)
    else:
        print("False value: ",v)
        
# ! None is like undef or Null or Nill in other languages