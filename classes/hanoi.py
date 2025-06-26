import tkinter as tk
from tkinter import font
from classes.disques import *
import time


class Hanoi:
    def __init__(self, nbdisques):
        self.disques = [[], [], []]
        for taille in range(nbdisques):
            self.disques[0].append(Disques(taille + 1))
        self.nbdisques = len(self.disques[0])

        self.tk = tk
        self.root = self.tk.Tk()
        self.root.resizable(False, False)
        self.canvas = self.tk.Canvas(self.root, width=800, height=250)
        self.canvas.pack()
        self.text = tk.Label(
            self.root,
            text="                                                            Les tours de Hanoï avec %s disques...                                                            "
            % self.nbdisques,
            background="orangered",
            foreground="white",
            font=font.Font(family="Source Code Pro", size="14"),
        )
        self.text.place(relx=0.5, rely=1, y=-17, anchor="center")
        self.root.title("Hanoï : %s disque.s" % self.nbdisques)
        self.buildCanvas()
        self.root.update()

    def __str__(self):
        return str(self.disques)

    def jouer(self):
        self.afficher()
        self.root.update()

        def bouge(x, y):
            """
            Fonction qui "déplace" les disques si c'est possible
            """
            if self.disques[x] != [] and self.disques[y] == []:
                self.disques[y].insert(0, self.disques[x].pop(0))
                self.afficher()
                self.root.update()
                return True

            elif (
                self.disques[x] != []
                and self.disques[x][0].taille < self.disques[y][0].taille
            ):
                self.disques[y].insert(0, self.disques[x].pop(0))
                self.afficher()
                self.root.update()
                return True

            else:
                return False

        def deplace2pions(depart, arrivee, intermediaire):
            """
            Fonction qui permet de deplacer deux disques si c'est possible
            """
            if bouge(depart, intermediaire) == False:
                return "Erreur 1 deplacer2pions() %(departTaille)s %(interTaille)s" % {
                    "departTaille": self.disques[depart][0].taille,
                    "interTaille": self.disques[intermediaire][0].taille,
                }
            if bouge(depart, arrivee) == False:
                bouge(intermediaire, depart)
                return "Erreur 2 deplacer2pions() %(interTaille)s %(departTaille)s" % {
                    "interTaille": self.disques[intermediaire][0].taille,
                    "departTaille": self.disques[depart][0].taille,
                }
            if bouge(intermediaire, arrivee) == False:
                bouge(arrivee, depart)
                bouge(intermediaire, depart)
                return "Erreur 1 deplacer2pions() %(interTaille)s %(arriveeTaille)s" % {
                    "interTaille": self.disques[intermediaire][0].taille,
                    "arriveeTaille": self.disques[arrivee][0].taille,
                }
            return "OK"

        def deplaceNpions(n, depart, arrivee, intermediaire):
            """
            La fameuse fonction récursive qui permet de déplacer N disques
            """
            if n > self.nbdisques:
                print(
                    "Impossible de deplacer %(n)s disques, puisqu'il y en a %(nbdisques)s"
                    % {"n": n, "nbdisques": self.nbdisques}
                )
                return
            if n == 0:
                return
            if n == 1:
                bouge(depart, arrivee)
                return
            if n == 2:
                deplace2pions(depart, arrivee, intermediaire)
                return
            else:
                deplaceNpions(n - 1, depart, intermediaire, arrivee)
                bouge(depart, arrivee)
                deplaceNpions(n - 1, intermediaire, arrivee, depart)

        deplaceNpions(self.nbdisques, 0, 2, 1)

    def afficher(self):
        self.buildCanvas()

        time.sleep(0.1)
        self.root.update()

    def buildCanvas(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(150, 200, 150, 50)
        self.canvas.create_rectangle(400, 200, 400, 50)
        self.canvas.create_rectangle(650, 200, 650, 50)
        self.canvas.create_rectangle(50, 200, 750, 200)

        for tour in range(len(self.disques)):
            for disque in range(len(self.disques[tour])):
                taille = self.disques[tour][-1 - disque].taille + 1.5
                largeur = taille * 20
                hauteur = 20
                x = 150 + tour * 250 - taille * 10
                y = 200 - hauteur * (disque + 1)
                self.canvas.create_rectangle(
                    x,
                    y,
                    x + largeur,
                    y + hauteur,
                    fill=self.disques[tour][-1 - disque].couleur,
                )
