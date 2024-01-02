"""
Auteur : Enis Béziau
Jeu du morpion en 1 contre 1 fait avec tkinter
"""

import tkinter as tk
from tkinter import messagebox


class Morpion:

    def __init__(self):
        self.fen = tk.Tk()
        self.ensemble_btn = []
        self.joueur_courant = 'X'
        self.victoire = False
        self.fen.minsize(500, 500)
        self.dessiner_grille()

    def fin_partie(self, etat=None) -> None:
        """Fonction affichant un message de victoire ou de match nul"""
        if etat is None:
            messagebox.showinfo("Fin de partie", f"Le joueur {self.joueur_courant} a gagné le jeu")
        elif etat is None:
            messagebox.showinfo("Fin de partie", "Match nul !")
        self.fen.quit()
        return None

    def changer_joueur(self) -> None:
        """Change le joueur à chaque tour"""
        self.joueur_courant = 'O' if self.joueur_courant == 'X' else 'X'
        return None

    def verif_victoire(self, ligne_clic: int, colonne_clic: int) -> None:
        """Vérifie si le plateau est en position de victoire ou de match nul"""
        compteur = 0
        for i in range(3):
            btn = self.ensemble_btn[i][ligne_clic]
            if btn['text'] == self.joueur_courant:
                compteur += 1
        if compteur == 3:
            self.fin_partie()

        compteur = 0
        for i in range(3):
            btn = self.ensemble_btn[colonne_clic][i]
            if btn['text'] == self.joueur_courant:
                compteur += 1
        if compteur == 3:
            self.fin_partie()

        compteur = 0
        for i in range(3):
            btn = self.ensemble_btn[i][i]
            if btn['text'] == self.joueur_courant:
                compteur += 1
        if compteur == 3:
            self.fin_partie()

        compteur = 0
        for i in range(3):
            btn = self.ensemble_btn[2 - i][i]
            if btn['text'] == self.joueur_courant:
                compteur += 1
        if compteur == 3:
            self.fin_partie()

        if not self.victoire:
            compteur = 0
            for col in range(3):
                for ligne in range(3):
                    btn = self.ensemble_btn[col][ligne]
                    if btn['text'] == 'X' or btn['text'] == 'O':
                        compteur += 1
            if compteur == 9:
                self.fin_partie("nul")
        return None

    def placer_symbole(self, ligne: int, colonne: int) -> None:
        """Place un symbole dans la case cliquée en fonction du joueur courant"""
        btn_clic = self.ensemble_btn[colonne][ligne]
        if btn_clic['text'] == '':
            btn_clic.config(text=self.joueur_courant)
            self.verif_victoire(ligne, colonne)
            self.changer_joueur()
        return None

    def dessiner_grille(self) -> None:
        """Crée le plateau de jeu et stocke les btns crées dans une matrice"""
        for col in range(3):
            btn_dans_col = []
            for ligne in range(3):
                btn = tk.Button(
                    self.fen,
                    font=('Arial', 50),
                    width=5, height=3,
                    command=lambda li=ligne, c=col: self.placer_symbole(li, c)
                )
                btn.grid(row=ligne, column=col)
                btn_dans_col.append(btn)
            self.ensemble_btn.append(btn_dans_col)
        return None

    def run(self) -> None:
        """Lance le jeu"""
        self.fen.mainloop()
        return None


if __name__ == '__main__':
    game = Morpion()
    game.run()
