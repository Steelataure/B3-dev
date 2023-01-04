import tkinter as tk

class Application(tk.Tk):

    def __init__(self, largeur=720, hauteur=630):
        self.root = tk.Tk()
        #self.iconbitmap('assets/logo.ico')
        self.root.resizable(False, False)
        self.root.title("Générateur de calcul mental")
        self.largeur = largeur
        self.hauteur = hauteur
        self.root.geometry("{}x{}".format(str(largeur),str(hauteur)))