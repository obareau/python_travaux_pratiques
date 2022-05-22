stack = []

stack.append("Joe")
print(stack)
stack.append("Jane")
print(stack)
stack.append("Bob")
print(stack)
while stack:
    name = stack.pop() # Remove lasty item
    print(name) # Print poped item
    print(stack)    # print stack until it's empty