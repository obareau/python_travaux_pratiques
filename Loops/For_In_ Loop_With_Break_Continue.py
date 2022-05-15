txt = "hello world"
for c in  txt:
    if c == " ":
        continue
    if c == "r":
        break
    print(c)
print("DONE")
