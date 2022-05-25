nbCarMax = 30 # nombre maximum de caractères considérés
print ("donnez un mot écrit en minuscules, terminé par un espace :")
mot = input() 
fini = False
i = 0
while not fini :
    c = mot[i] # on prend le ième caractère (le premier est de rang 0)
    if c=="a" or c=="e" or c=="i" or c=="o" or c=="u" or c=="y" :
        print (c)
    if c==" " or i >= nbCarMax-1 :
        fini = True
        i = i + 1