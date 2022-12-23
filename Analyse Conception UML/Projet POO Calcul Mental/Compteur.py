import time

class Compteur():
    def __init__(self, compteur_now=20, compteur_max=0):
        self.compteur_now = compteur_now
        self.compteur_max = compteur_max

    def getCompteur(self):
        if self.compteur_now > self.compteur_max:
            self.compteur_now -= 0.5
            return self.compteur_now
        if self.compteur_now == 0:
            return "fin"
        