import pygame
import sys
from button import *
from button import Button
from ground import Ground
from player import Player


class Game:

    def __init__(self):
        # Configuration de la taille de la fenêtre
        self.screen = pygame.display.set_mode((1400, 900))
        pygame.display.set_caption("Page d'accueil")
        self.running = True
        self.player_x, self.player_y = 600, 400
        self.height = [32, 64]
        self.player = Player(self.player_x, self.player_y, self.height)

    # Boucle principale
    def main(self):

        # Création des instances de la classe Bouton
        playButton = Button("Jouer", 550, 380, 300, 50, (0, 128, 255), playFunction)
        creditButton = Button("Crédits", 550, 480, 300, 50, (0, 128, 255), creditFunction)

        # Définition des couleurs
        white: tuple[int, int, int] = (255, 255, 255)
        black: tuple[int, int, int] = (0, 0, 0)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Clic sur le bouton Jouer
                    if playButton.x < x < playButton.x + playButton.largeur and playButton.y < y < playButton.y + playButton.hauteur:
                        playButton.fonction()
                    # Clic sur le bouton Crédits
                    elif creditButton.x < x < creditButton.x + creditButton.largeur and creditButton.y < y < creditButton.y + creditButton.hauteur:
                        creditButton.fonction()
                    # Clic sur la croix de fermeture de fenêtre
                    elif 1400 - closeButtonWidth < x < 1400 and 0 < y < closeButtonHeight:
                        self.running = False

            self.screen.fill(black)
            self.player.show(self.screen)

            # Dessine les boutons
            playButton.drawButton(self.screen, white)
            creditButton.drawButton(self.screen, white)

            # Chargement de l'image de la croix de fermeture
            close_button = pygame.image.load("Images/close_button.png")
            # Redimensionnement de l'image de la croix de fermeture
            closeButtonWidth = 30  # Spécifiez la nouvelle largeur souhaitée
            closeButtonHeight = 30  # Spécifiez la nouvelle hauteur souhaitée
            close_button = pygame.transform.scale(close_button, (closeButtonWidth, closeButtonHeight))

            # Affiche le bouton de fermeture redimensionné en haut à droite
            self.screen.blit(close_button, (1400 - closeButtonWidth, 0))

            # Rafraîchit l'écran
            pygame.display.flip()


# Lancement
if __name__ == '__main__':
    pygame.init()
    Game().main()
    pygame.quit()
