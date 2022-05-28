from math import sqrt
from tomatholive import sqr


class Point(object):
    """Définition d'un point mathématique"""

    def __init__(self, xx=0, yy=0):
        self.x = xx
        self.y = yy

    def distance(self, p2):
        """Calcule la distance Euclidienne"""
        print("[P1] coord. horizontale = ", self.x, "coord. verticale =", self.y)
        print("[P2] coord. horizontale = ", p2.x, "coord. verticale =", p2.y)
        print("[Distance Euclidienne]  = ", sqrt(sqr(p2.y - self.y) + sqr(p2.x - self.x)))

        return sqrt(sqr(p2.y - self.y) + sqr(p2.x - self.x))


oPoint9 = Point(0,0)  # p9 instance de la classe Point()
oPoint10 = Point(10,10)  # p10 instance de la classe Point()



Point.distance(oPoint9, oPoint10)
# ToDO p1.distance(p2)
