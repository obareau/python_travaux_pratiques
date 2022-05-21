animals = ['chicken', 'cow', 'snail', 'elephant']
print(animals)

animals.sort()
print(animals)

animals.sort(key=len)
print(animals)
animals.sort(key=len, reverse=True) # sort by char_item length
print(animals)
# 1 ['chicken', 'cow', 'snail', 'elephant']
# 2 ['chicken', 'cow', 'elephant', 'snail']
# 3 ['cow', 'snail', 'chicken', 'elephant']
# 4 ['elephant', 'chicken', 'snail', 'cow']