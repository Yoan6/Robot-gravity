import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Configuration de la taille de la fenêtre
largeur_fenetre = 1400  # Spécifiez la largeur souhaitée
hauteur_fenetre = 900  # Spécifiez la hauteur souhaitée
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Page d'accueil")

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Chargement de l'image de la croix de fermeture
close_button = pygame.image.load("Images/close_button.png")

# Redimensionnement de l'image de la croix de fermeture
largeur_close_button = 30  # Spécifiez la nouvelle largeur souhaitée
longueur_close_button = 30  # Spécifiez la nouvelle hauteur souhaitée
close_button = pygame.transform.scale(close_button, (largeur_close_button, longueur_close_button))

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

# Création des instances de la classe Bouton
bouton_jouer = Bouton("Jouer", 550, 380, 300, 50, (0, 128, 255), fonction_jouer)
bouton_credits = Bouton("Crédits", 550, 480, 300, 50, (0, 128, 255), fonction_credits)

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Clic sur le bouton Jouer
            if bouton_jouer.x < x < bouton_jouer.x + bouton_jouer.largeur and bouton_jouer.y < y < bouton_jouer.y + bouton_jouer.hauteur:
                bouton_jouer.fonction()
            # Clic sur le bouton Crédits
            elif bouton_credits.x < x < bouton_credits.x + bouton_credits.largeur and bouton_credits.y < y < bouton_credits.y + bouton_credits.hauteur:
                bouton_credits.fonction()
            # Clic sur la croix de fermeture de fenêtre
            elif largeur_fenetre - largeur_close_button < x < largeur_fenetre and 0 < y < longueur_close_button:
                en_cours = False

    # Efface l'écran
    fenetre.fill(NOIR)

    # Dessine les boutons
    bouton_jouer.dessiner(fenetre)
    bouton_credits.dessiner(fenetre)

    # Affiche le bouton de fermeture redimensionné en haut à droite
    fenetre.blit(close_button, (largeur_fenetre - largeur_close_button, 0))

    # Rafraîchit l'écran
    pygame.display.flip()

# Quitte Pygame
pygame.quit()
sys.exit()
