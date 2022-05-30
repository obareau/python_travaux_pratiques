
from random import *
# Create a dictionary with Values

class Entity(object):
    """Définit l'ensemble des personnages"""

    def __init__(self, oname = "Toto", ohealth = 25, oxp = 1 ):
        self.name = oname
        self.health = ohealth
        self.ini = 0
        self.xp = oxp
        self.attack = 12
        self.dammage = 0

    def Initiative(self):
        self.ini = randrange(0, 2)
        
    
    def Attack(self,victim):
        hit = randrange(0, self.attack)
        print(f"Attaque : {self.name}, {hit}")
        victim.health = victim.health - hit
        print(f"Santé : {victim.name}", victim.health)



# Todo Name definition (input name)
Pj = Entity(oname="titi")
Enemy = Entity(oname="grominet")

# # Who plays first
# Pj.Initiative()
# Enemy.Initiative()



# if Pj.ini > Enemy.ini :
#     print("Pj attack first")
#     Pj.Attack(who = Enemy)
    
# else:
#     print("Enemy attack first")
#     Enemy.Attack(who = Pj)

while Pj.health > 0 and Enemy.health > 0:
    Pj.Attack(victim = Enemy)
    Enemy.Attack(victim = Pj)
    
if Pj.health >  Enemy.health:
    print("J'ai gagné")
    
else:
    print("J'ai perdu")