import pygame


# Classe pour représenter un bouton
def playFunction():
    print("Bouton Jouer cliqué")
    # Ajouter ici le code pour la fonction "Jouer"


def creditFunction():
    print("Bouton Crédits cliqué")
    # Ajouter ici le code pour la fonction "Crédits"


class Button:
    def __init__(self, texte, x, y, largeur, hauteur, couleur):
        self.texte = texte
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur

    def draw(self, surface, colorTxt):
        pygame.draw.rect(surface, self.couleur, (self.x, self.y, self.largeur, self.hauteur))
        font = pygame.font.Font(None, 36)
        texte_surface = font.render(self.texte, True, colorTxt)
        texte_rect = texte_surface.get_rect()
        texte_rect.center = (self.x + self.largeur / 2, self.y + self.hauteur / 2)
        surface.blit(texte_surface, texte_rect)

    def erase_button(self):
        self.x = 0
        self.y = 0
        self.largeur = 0
        self.hauteur = 0
