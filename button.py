import pygame
import sys

# Classe pour représenter un bouton
def playFunction():
    print("Bouton Jouer cliqué")
    # Ajoutez ici le code pour la fonction "Jouer"


def creditFunction():
    print("Bouton Crédits cliqué")
    # Ajoutez ici le code pour la fonction "Crédits"


class Button:
    def __init__(self, texte, x, y, largeur, hauteur, couleur, fonction):
        self.texte = texte
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.fonction = fonction

    def drawButton(self, surface, colorTxt):
        pygame.draw.rect(surface, self.couleur, (self.x, self.y, self.largeur, self.hauteur))
        font = pygame.font.Font(None, 36)
        texte_surface = font.render(self.texte, True, colorTxt)
        texte_rect = texte_surface.get_rect()
        texte_rect.center = (self.x + self.largeur / 2, self.y + self.hauteur / 2)
        surface.blit(texte_surface, texte_rect)

