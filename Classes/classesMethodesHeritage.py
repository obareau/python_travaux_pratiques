class Time(object):
    """Classe temporelle"""

    def __init__(self, hh=0, mm=0, ss=0):
        self.heure = hh
        self.minute = mm
        self.seconde = ss

    def afficheHeure(self):
        
        print("%s:%s:%s" % (self.heure, self.minute, self.seconde))


maintenant = Time() 

maintenant.afficheHeure() # 0:0:0

recree = Time(10, 30) 

recree.afficheHeure() # 10:30:0
