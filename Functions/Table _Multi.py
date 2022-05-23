# def table(base):
#     "donne les 10 premiers mulltiple de base(n)"
#     n = 1
#     while n < 11 : 
#         print (n * base) 
#         n = n + 1
        
#         print("---")
        
# table(7)

# print("---")

# a = 1
# while a < 20:
#     table(a)
#     a = a + 1
#     print(f"table de base {a}")

def table(base):
    "Donne les 10 premiers mulltiple de base(n)"
    result = [] # result est d’abord une liste vide
    n = 1
    while n < 11:
        b = n * base
        result.append(b) # ajout d’un terme à la liste
        n = n +1 # (voir explications ci-dessous)
    return result

ta9 = table(9)
print(ta9)