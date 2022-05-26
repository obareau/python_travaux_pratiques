from math import sqrt
from tomatholive import sqr

class Point(object):
    "Définition d'un point mathématique"



    def distance(self, p2):
        "Calcule la distance entre 2 points dans un espace 2d"
        print("[P1] coord. horizontale = ", self.x, "coord. verticale =", self.y)
        print("[P2] coord. horizontale = ", p2.x, "coord. verticale =", p2.y)
        print("[Distance Euclidienne]  = ", sqrt(sqr(p2.y - self.y) + sqr(p2.x - self.x)))

        return sqrt(sqr(p2.y - self.y) + sqr(p2.x - self.x))


oPoint9 = Point()  # p9 instance de la classe Point()
oPoint10 = Point()  # p10 instance de la classe Point()

oPoint9.x = 0.0
oPoint9.y = 0.0

oPoint10.x = 10.0
oPoint10.y = 10.0


Point.distance(oPoint9, oPoint10)
