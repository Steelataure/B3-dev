import tkinter as tk
from tkinter import *
import random
import time

noir = "black"
blanc = "white"
 

class Application(object):
    def __init__(self, largeur=720, hauteur=630):
        self.root = tk.Tk()
        self.root.title("Générateur de calcul mental")
        self.largeur = largeur
        self.hauteur = hauteur
        self.root.geometry("{}x{}".format(str(largeur),str(hauteur)))

        pre_number = random.randint(1,500)
        self.pre_number = pre_number

        post_number = random.randint(1,500)
        self.post_number = post_number

        operateur = ["+", "-", "/", "*"]
        self.operateur = operateur

        self.operateur_choice = random.choice(self.operateur)
        operateur_choice = self.operateur_choice


    def generate_operation(self):
        all_operation = str(self.pre_number) + self.operateur_choice + str(self.post_number)
        return all_operation

    def verif_operation(self):
        correction = eval(str(self.pre_number) + self.operateur_choice + str(self.post_number))
        return correction

    def affichage(self):
        self.generate = tk.Label(self.root, text=self.generate_operation(), fg=noir, height=5).pack()
        #ICI TU RAJOUTES LES AUTRES CHAMPS


        self.root.mainloop()


""" 
class Compteur(): 
    def __init__(self, compteur_start = 10, compteur_stop = 0):

        self.compteur_start = compteur_start
        self.compteur_stop = compteur_stop

    def compteur_avancement(self):
        while self.compteur_start >= self.compteur_stop:

            self.affichage['text'] = str(self.compteur_start)
            self.compteur += 1
            root.affichage.update_idletasks()
            time.sleep(1)
            return self 
            """


class User(): 
    def __init__(self):
        pass

    def reponse_operation():
        pass


if __name__ == "__main__":

    root = Application()
    #root.correction()
    root.affichage()
    print(root.verif_operation())
