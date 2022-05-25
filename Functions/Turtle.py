from dessins_tortue import *
up()
goto(-150,50)
# relever le crayon
# reculer en haut à gauche
# dessiner dix carrés rouges, alignés :
i = 0
while i < 10:
    down()
     # abaisser le crayon
    star5(50, 'red', 0)
     # tracer un carré
    up()
     # relever le crayon
    forward(60)
     # avancer + loin
    i = i +1
a = input()
 # attendre