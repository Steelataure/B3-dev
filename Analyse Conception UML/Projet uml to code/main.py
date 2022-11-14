
import tkinter as tk

from tkinter import *



class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)


def main():
    app = Application()
    app.title("Calcul mental")
    app.geometry('720x630')
    app.resizable(False, False)

    app.mainloop()


if __name__ == '__main__':
    main()