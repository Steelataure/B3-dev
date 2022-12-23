import tkinter as tk
from tkinter import *

from Operation import *
from Compteur import *

noir = "black"
blanc = "#f4f4f4"
 

class Programme(tk.Tk):
    def __init__(self, largeur=720, hauteur=630):
        tk.Tk.__init__(self)

        self.iconbitmap('assets/logo.ico')
        self.resizable(False, False)
        self.title("Générateur de calcul mental")
        self.largeur = largeur
        self.hauteur = hauteur

        self.geometry("{}x{}".format(str(largeur),str(hauteur)))

        self.operation = Operation()
        self.compteur = Compteur()

        self.affichage()
        self.affiche_compteur()
        
    def verif_operation(self):
        correction = eval(self.operation.generate_operation())
        return correction
   
    def win_condition(self):
        if self.getReponseUser() == str(self.verif_operation()) and not self.LOSS:
            self.correction = tk.Label(self, text="Bravo, bonne réponse", fg="green", bg=blanc, font=("Franklin Gothic Demi", 18)).place(x=250, y=364)
        else: 
            self.correction = tk.Label(self, text=f"Dommage, voici la correction : {self.verif_operation()}", fg="green", bg=blanc, font=("Franklin Gothic Demi", 18)).place(x=170, y=364)
            self.LOSS = 1

    def getReponseUser(self):
        self.input_value = self.my_input.get()
        return self.input_value

    def getOperation(self):
        return self.operation.generate_operation()

    def getCompteur(self):
        return self.compteur.getCompteur()


    def affichage(self):
        self.background = PhotoImage(file = "assets/apercu3.png")
        tk.Label(self, image = self.background).place(x = -2, y = -1)

        self.my_label = Label(self, text="Veuillez résoudre l'opération", fg="green", bg=blanc, 
        font=("Franklin Gothic Demi", 18)).place(x=205, y=205)
        
        self.generate = Label(self, text=self.operation.generate_operation(), 
        font=("Franklin Gothic Demi", 18), fg=noir).place(x = 300, y = 250)

        self.my_input = tk.Entry(self, width= 27, font=("Franklin Gothic Demi", 18))
        self.my_input.place(x=162, y=310, height = 40)

        self.Start_image = PhotoImage(file='assets/start.png')
        self.Button_start = tk.Button(self, image=self.Start_image, borderwidth=0, bg=blanc, activebackground='WHITE', command=lambda:[self.getReponseUser(), self.win_condition()]).place(x=210, y=420)
            
    def affiche_compteur(self):
        self.affiche_compteur = Label(self, text=self.compteur.getCompteur(), 
        font=("Franklin Gothic Demi", 18), fg=noir).place(x = 300, y = 200)

    def display_update(self):
        for i in range(20):
            self.after(1000, self.affiche_compteur)
            self.update()

            print(self.getCompteur())
