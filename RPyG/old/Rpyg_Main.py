import random


class Pj(object):
    """Définit le personnage jouable"""

    def __init__(self):
        self.Pv = 30
        self.Xp = 1
        
    def printDommage(self): 
        """affiche dommage"""
        print("[Dommage] = ", self.dammage())        

    def dammage(self):
        # maxrange = 12
        # pt_attack = random.randrange(maxrange)
        # Xp = 1  # we will work on that later
        # print(pt_attack)
        return random.randrange(0, 12)
        # return 10

    def health(self):

        # new_health = self.Pv - self.dammage()
        # print(new_health)
        return self.Pv - self.dammage()


p1 = Pj()

p1.pprint()


if p1.dammage() >= 10:
    print("Critical hit")

if p1.health() <= 20:
    print(" Pj is seriously wounded")

# p1.pprint()

#     else:
#         p1.dammage
#         p1.health = p1.health() - 1
