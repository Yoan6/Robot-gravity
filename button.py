import pygame

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

