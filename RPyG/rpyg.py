
from random import *
# Create a dictionary with Values

class Entity(object):
    """Définit l'ensemble des personnages"""

    def __init__(self, oname = "Toto", ohealth = 25, oxp = 1 ):
        self.name = oname
        self.health = ohealth
        self.ini = 0
        self.xp = oxp
        self.attack = 0
        self.dammage = 0

    def Initiative(self):
        self.ini = randrange(0, 2)
        
    
    def Attack(self):
        self.attack = randrange(0, 12)

    def Dammage(self, who):
        self.dammage = who.health - self.attack



# Todo Name definition (input name)
Pj = Entity(oname="titi")
Enemy = Entity(oname="grominet")

# Who play first
Pj.Initiative()
Enemy.Initiative()

if Pj.ini > Enemy.ini :
    print("Pj attack first")
    
else:
    print("Enemy attack first")