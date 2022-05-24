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
    carre(25, 'red')
     # tracer un carré
    up()
     # relever le crayon
    forward(30)
     # avancer + loin
    i = i +1
a = input()
 # attendre