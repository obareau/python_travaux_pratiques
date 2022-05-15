txt = "hello world"
for c in txt:
    if c == " ":
        continue
    print(c)
    # ! Will print every single chars from txt  EXCEPT  space
    