text = "The black cat climbed the green tree."
T_Len = len(text)
print (T_Len)
start = 0
while True:
    loc = text.find("e", start)
    if loc == -1:
        break
    print(loc)
    start = loc + 1