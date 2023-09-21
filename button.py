import pygame


# Classe pour représenter un bouton

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
        lines = self.texte.split('\n')  # Sépare le texte en lignes sur les sauts de ligne
        y_offset = 0
        for line in lines:
            texte_surface = font.render(line, True, colorTxt)
            texte_rect = texte_surface.get_rect()
            texte_rect.center = (self.x + self.largeur / 2, self.y + self.hauteur / 2 + y_offset)
            surface.blit(texte_surface, texte_rect)
            y_offset += 25  # Espacement vertical entre les lignes

    def erase_button(self):
        self.x = 0
        self.y = 0
        self.largeur = 0
        self.hauteur = 0
