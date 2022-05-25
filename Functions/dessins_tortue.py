from turtle import *

def carre(taille, couleur, angle):
    "fonction qui dessine un carré de taille, angle et de couleur déterminées"
    color(couleur)
    c =0
    
    while c <4:
        forward(taille)
        right(90)
        c = c +1
        
def triangle(taille, couleur, angle):
    "Fonction qui dessine un triangle de taille, angle et couleur détérminé"
    color(couleur)
    c = 0
    
    while c <3:
        forward(taille)
        right(120)
        c = c + 1
        
def star5(taille, couleur, angle):
    "Fonction qui dessine une étoile à 5 branches de taille, angle et couleur détérminé"
    color(couleur)
    c = 0
    
    while c <5:
        forward(taille)
        left(144)
        c = c + 1        