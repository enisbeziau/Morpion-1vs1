"""
Auteur : Enis Béziau
Jeu du morpion en 1 vs 1 fait avec Tkinter
"""


import tkinter
from tkinter import messagebox  # Pour le pop up de victoire


class Morpion:
    def __init__(self):
        self.grp_btns = []
        self.joueur_courant = 'X'
        self.victoire = False
        self.fen = tkinter.Tk()
        self.fen.minsize(500, 500)
        self.dessiner_grille()

    def print_winner(self):
        """Affiche le message de fin donnant le nom du grand gagnant"""
        if not self.victoire:
            self.victoire = True
            messagebox.showinfo("Fin de partie", f"Le joueur {self.joueur_courant} a gagné le jeu")
            self.fen.quit()
        return None

    def changer_joueur(self) -> None:
        """Change le joueur courant"""
        if self.joueur_courant == 'X':
            self.joueur_courant = 'O'
        else:
            self.joueur_courant = 'X'
        return None

    def check_win(self, clicked_row: int, clicked_col: int) -> None:
        """Vérifie si le plateau comporte des positions de victoire / de match nul"""
        # Detecter victoire horizontale
        if all(button['text'] == self.joueur_courant for button in self.grp_btns[clicked_col]):
            self.print_winner()

        # Detecter victoire verticale
        if all(self.grp_btns[clicked_col][i]['text'] == self.joueur_courant for i in range(3)):
            self.print_winner()

        # Detecter victoire diagonale
        if clicked_row == clicked_col == 1 or clicked_row != clicked_col:
            if all(self.grp_btns[i][i]['text'] == self.joueur_courant for i in range(3)):
                self.print_winner()

        # Detecter victoire diagonale inverse
        if clicked_row == 1 and clicked_col == 1 or abs(clicked_row - clicked_col) == 2:
            if all(self.grp_btns[2 - i][i]['text'] == self.joueur_courant for i in range(3)):
                self.print_winner()

        # Verifier match nul
        if not self.victoire and all(button['text'] in ('X', 'O') for row in self.grp_btns for button in row):
            print("Match nul")
        
        return None

    def placer_element(self, ligne: int, colonne: int) -> None:
        """Place une croix 'X' ou un rond 'O' en fonction du clique et du joueur courant"""
        btn_clic = self.grp_btns[colonne][ligne]
        if btn_clic['text'] == "":
            btn_clic.config(text=self.joueur_courant)
            self.check_win(ligne, colonne)
            self.changer_joueur()
        return None

    def dessiner_grille(self) -> None:
        """Dessine la grille du plateau étant composée de 3x3 boutons"""
        for colonne in range(3):
            buttons_in_cols = []
            for row in range(3):
                button = tkinter.Button(
                    self.fen, font=("Arial", 50),
                    width=5, height=3,
                    command=lambda r=row, c=colonne: self.placer_element(r, c)
                )
                button.grid(row=row, column=colonne)
                buttons_in_cols.append(button)
            self.grp_btns.append(buttons_in_cols)
        return None

    def run(self) -> None:
        """Lance le jeu"""
        self.fen.mainloop()
        return None


if __name__ == "__main__":
    game = Morpion()
    game.run()
