from turtle import *
def carre(taille, couleur):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    c =0
    
    while c <4:
        forward(taille)
        right(90)
        c = c +1