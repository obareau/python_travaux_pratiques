# split and extend
# When collecting data which is received from a string via splitting,
# we would like to add the new elements to the existing list

lines = [
    'abc def ghi',
    'hello world',
]

collector = []

for l in lines:
    collector.extend(l.split())
    print(collector)

# ['abc', 'def', 'ghi']
# ['abc', 'def', 'ghi', 'hello', 'world']