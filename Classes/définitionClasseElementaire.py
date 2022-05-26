from math import sqrt


# ! object = data plus code THAT act on  THAT data over time

class Point(object): # nom de classe commence par majuscule // object classe ancêtre si on veut hériter d'une autre classe la spécifier dans ()
    #  Identation obligatoire et au moins 1 ligne
    "Définition d'un point mathématique" # affiche la doc dans IDE digne de ce nom
    

# As a naming convention in this book, I will generally use the prefix of a lowercase o
# to denote a variable that represents an object. This is not required, but it’s a way to
# remind myself that the variable represents an obj

oPoint9 = Point() # p9 instance de la classe Point()
oPoint10 = Point() # p10 instance de la classe Point()
    
print(oPoint9) 
# Le message renvoyé par Python indique, comme vous l’aurez certainement bien compris tout de suite,
# que p9 est une instance de la classe Point(), laquelle est définie elle-même au niveau principal (main) du
# programme. Elle est située dans un emplacement bien déterminé de la mémoire vive, dont l’adresse apparaît ici en notation hexadécimale.

print(oPoint9.__doc__)
# Comme nous l’avons expliqué pour les fonctions (cf. page 60), les chaînes de documentation de divers
# objets Python sont associées à l’attribut prédéfini __doc__. Il est donc toujours possible de retrouver la
# documentation associée à un objet Python quelconque, en invoquant cet attribut.

# Attributs (ou variables) d’instance
# L’objet que nous venons de créer est juste une coquille vide. Nous allons à présent lui ajouter des composants, par simple assignation, en utilisant le système de qualification des noms par points

oPoint9.x = 0.0
oPoint9.y = 0.0

oPoint10.x = 10.0
oPoint10.y = 10.0

# Les variables x et y que nous avons ainsi définies en les liant d’emblée à
# p9 , sont désormais des attributs de l’objet p9. On peut également les appeler des variables d’instance. Elles sont en effet incorporées, ou plutôt
# encapsulées dans cette instance (ou objet). Le diagramme d’état ci-contre
# montre le résultat de ces affectations : la variable p9 contient la référence
# indiquant l’emplacement mémoire du nouvel objet, qui contient luimême les deux attributs x et y.

print(oPoint9.x, oPoint9.y)

x = oPoint9.x
print(x)
print(x+1)
# oPoint9.x = x + 2
# print(oPoint9.x)

# Passage d’objets comme arguments lors de l’appel d’une fonction
# Les fonctions peuvent utiliser des objets comme paramètres, et elles peuvent également fournir un objet comme valeur de retour. Par exemple, vous pouvez définir une fonction telle que celle-ci

def affiche_point(p):
    print ("coord. horizontale =", p.x, "coord. verticale =", p.y)
    
# affiche_point(oPoint9)

def Sqr(a):
    "mettre au carré"
    return a*a

def calculDistance2pts(p1, p2):
    "Calcule la distance entre 2 points dans un espace 2d"
    print ("[P1] coord. horizontale = ", p1.x, "coord. verticale =", p1.y)
    print ("[P2] coord. horizontale = ", p2.x, "coord. verticale =", p2.y)
    print ("[Distance Euclidienne]  = ", sqrt(Sqr(p2.y-p1.y)+Sqr(p2.x-p1.x)))
    return sqrt(Sqr(p2.y-p1.y)+Sqr(p2.x-p1.x))

calculDistance2pts(oPoint9, oPoint10)