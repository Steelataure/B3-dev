import tkinter as tk
from tkinter import *
import random
import time

noir = "black"
blanc = "white"
 

class Application(object):
    def __init__(self, largeur=720, hauteur=630, compteur_start = 10, compteur_stop = 0):
        self.root = tk.Tk()
        self.root.title("Générateur de calcul mental")
        self.largeur = largeur
        self.hauteur = hauteur
        self.root.geometry("{}x{}".format(str(largeur),str(hauteur)))


        self.compteur_start = compteur_start
        self.compteur_stop = compteur_stop

        
    def generate_operation(self):

        self.pre_number = random.randint(1,500)
        self.post_number = random.randint(1,500)
        self.operateur = ["+", "-", "/", "*"]
        self.operateur_choice = random.choice(self.operateur)
        all_operation = str(self.pre_number) + self.operateur_choice + str(self.post_number)

        return all_operation


    def verif_operation():
        pass

    def setAffichageCompteur(self, affichage_compteur):
        self.affichage_compteur = affichage_compteur

    def getAffichageCompteur(self):
        return self.affichage_compteur

    def compteur(self):
        self.compteur_start -=1
        


    def affichage(self):

        self.generate = tk.Label(self.root, text=self.generate_operation(), fg=noir, height=5).pack()
        self.affichage_compteur = tk.Label(self.root, text=str(self.compteur_start), fg=noir, height=10).pack()



        self.root.mainloop()


class User(): 
    def __init__(self):
        pass

    def reponse_operation():
        pass


if __name__ == "__main__":

    root = Application().affichage()
