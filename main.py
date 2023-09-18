import pygame
import sys
from button import *
from button import Button
from ground import Ground


# Initialisation de Pygame
pygame.init()

# Configuration de la taille de la fenêtre
windowWidth = 1400  # Spécifiez la largeur souhaitée
windowHeight = 900  # Spécifiez la hauteur souhaitée
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Page d'accueil")

# Définition des couleurs
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)

# Chargement de l'image de la croix de fermeture
close_button = pygame.image.load("Images/close_button.png")

# Redimensionnement de l'image de la croix de fermeture
closeButtonWidth = 30  # Spécifiez la nouvelle largeur souhaitée
closeButtonHeight = 30  # Spécifiez la nouvelle hauteur souhaitée
close_button = pygame.transform.scale(close_button, (closeButtonWidth, closeButtonHeight))


# Création des instances de la classe Bouton
playButton = Button("Jouer", 550, 380, 300, 50, (0, 128, 255), playFunction)
creditButton = Button("Crédits", 550, 480, 300, 50, (0, 128, 255), creditFunction)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Clic sur le bouton Jouer
            if playButton.x < x < playButton.x + playButton.largeur and playButton.y < y < playButton.y + playButton.hauteur:
                playButton.fonction()
            # Clic sur le bouton Crédits
            elif creditButton.x < x < creditButton.x + creditButton.largeur and creditButton.y < y < creditButton.y + creditButton.hauteur:
                creditButton.fonction()
            # Clic sur la croix de fermeture de fenêtre
            elif windowWidth - closeButtonWidth < x < windowWidth and 0 < y < closeButtonHeight:
                running = False

    # Efface l'écran
    window.fill(BLACK)

    # Dessine les boutons
    playButton.drawButton(window, WHITE)
    creditButton.drawButton(window, WHITE)

    # Affiche le bouton de fermeture redimensionné en haut à droite
    window.blit(close_button, (windowWidth - closeButtonWidth, 0))

    # Rafraîchit l'écran
    pygame.display.flip()

# Quitte Pygame
pygame.quit()
sys.exit()
