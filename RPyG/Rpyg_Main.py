import random

class Pj(object):
    "Définit le personnage jouable"

    def __init__(self):
        
        self.Pv = 25
        self.Xp =1
        
    
    def dammage(self):
        maxrange = 12
        pt_attack = random.randrange(0, maxrange+1) 
        xp = 1 # we will work on that later
        print(pt_attack)
        return pt_attack
    
    def health(self):
        take_dammage = Pj.Pv - Pj.dammage()
        
        print(take_dammage)
        return take_dammage

    
Pj1 = Pj()
Enemy1 = Pj()

while True:
    
    if Pj1.health() > 0:
        print("Pj is alive")
        break


# while True:
#     if  Pj1.health() >= 0 or Enemy1.health() >= 0 :
#         break
    
#     else:
#         Pj.Pj1.dammage()

# pj_attack = Pj1.Pv  - Pj1.dammage()
# print(pj_attack)

