# Classe pour représenter un bouton
class Bouton:
    def __init__(self, texte, x, y, largeur, hauteur, couleur, fonction):
        self.texte = texte
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.fonction = fonction

    def dessiner(self, surface):
        pygame.draw.rect(surface, self.couleur, (self.x, self.y, self.largeur, self.hauteur))
        font = pygame.font.Font(None, 36)
        texte_surface = font.render(self.texte, True, BLANC)
        texte_rect = texte_surface.get_rect()
        texte_rect.center = (self.x + self.largeur / 2, self.y + self.hauteur / 2)
        surface.blit(texte_surface, texte_rect)

    # Fonction pour la fonction "Jouer"
    def fonction_jouer():
        print("Bouton Jouer cliqué")
        # Ajoutez ici le code pour la fonction "Jouer"

    # Fonction pour la fonction "Crédits"
    def fonction_credits():
        print("Bouton Crédits cliqué")
        # Ajoutez ici le code pour la fonction "Crédits"