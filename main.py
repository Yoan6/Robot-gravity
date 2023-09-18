import pygame
import pytmx
from button import *
from button import Button
from player import *
from player import Player
from level import Level
from ground import Ground

class Game:
    def __init__(self):
        # Configuration de la taille de la fenêtre
        self.screen = pygame.display.set_mode((1400, 900))
        pygame.display.set_caption("Page d'accueil")
        self.running = True

    # Boucle principale
    def main(self):
        timer = pygame.time.Clock()
        # 1er niveau
        level1 = Level('Images/farm.png', self.screen)

        # On définit le groupe de sprite du robot :
        player_sprite = Player("Images/pnj.png", 200, 200, 248, 360)
        player_group = pygame.sprite.Group(player_sprite)

        # Définition des couleurs
        WHITE: tuple[int, int, int] = (255, 255, 255)
        BLACK: tuple[int, int, int] = (0, 0, 0)

        # Définition de la position horizontale de la caméra :
        camera_x = 0

        # Chargement de l'image de la croix de fermeture
        close_button = pygame.image.load("Images/close_button.png")

        # Redimensionnement de l'image de la croix de fermeture
        closeButtonWidth = 30  # Spécifiez la nouvelle largeur souhaitée
        closeButtonHeight = 30  # Spécifiez la nouvelle hauteur souhaitée
        close_button = pygame.transform.scale(close_button, (30, 30))


        # Variable pour indiquer si les boutons sont visibles ou non
        main_buttons_visible = True

        # Création des boutons de la page principale
        playButton = Button("Jouer", 550, 380, 300, 50, (0, 128, 255))
        creditButton = Button("Crédits", 550, 480, 300, 50, (0, 128, 255))
        # Création des boutons de la page principale

        # Boucle principale
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Clic sur le bouton Jouer
                    if playButton.x < x < playButton.x + playButton.largeur and playButton.y < y < playButton.y + playButton.hauteur:
                        main_buttons_visible = False
                        level1.run()

                    # Clic sur le bouton Crédits
                    elif creditButton.x < x < creditButton.x + creditButton.largeur and creditButton.y < y < creditButton.y + creditButton.hauteur:
                        print("Bouton Crédits cliqué")
                        # Ajoutez ici le code pour la fonction "Crédits"

                    # Clic sur la croix de fermeture de fenêtre
                    elif 1400 - closeButtonWidth < x < 1400 and 0 < y < closeButtonHeight:
                        self.running = False

            pygame.display.update()


            # Dessine les boutons
            if main_buttons_visible:
                playButton.draw(self.screen, WHITE)
                creditButton.draw(self.screen, WHITE)

            # Dessine le player :
            player_group.draw(self.screen)

            # Affiche le bouton de fermeture redimensionné en haut à droite
            self.screen.blit(close_button, (1400 - closeButtonWidth, 0))

            # On définis un laps de temps de 60 images par seconde par game loop
            timer.tick(60)

        # Écran noir
        self.screen.fill(BLACK)


# Lancement
if  __name__ == '__main__':
    pygame.init()
    Game().main()
    pygame.quit()
