# instead of substr'
text = "Hello world"

b = text[1:4]
print(b) # ell
print(text[2:]) # llo World
print(text[:2]) # He
start = 1
end = 4
print(text[start:end]) # ell
Negative_Index = -2
print(text[Negative_Index])