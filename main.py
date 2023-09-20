import pygame
import sys
import pytmx
from pygame.sprite import Group

from button import Button
from player import *
from player import Player
from level import Level
from ground import Ground
from obstacles import Spike
from advise import Advise
from plateform import Plateform


class Game:

    def __init__(self):
        # Configuration de la taille de la fenêtre
        self.screen = pygame.display.set_mode((1400, 900))
        pygame.display.set_caption("Page d'accueil")
        self.running = True
        self.player_x = 400
        self.player_y = 400
        self.playerSpeedX = 0
        self.taille = [32, 64]
        self.player = Player(self.player_x, self.player_y, self.taille)
        self.ground = Ground(0, 700, 1400, 900)
        self.gravity = (0, 10)
        self.resist = (0, 0)
        self.touchGround = False
        self.runningMusic = False
        self.rect = pygame.Rect(0, 0, 1400, 900)

        # 1 = vers le bas, autre = vers le haut
        self.gravityDirection = 1
        self.plateformListRect = [
            pygame.Rect(300, 500, 100, 50),
            pygame.Rect(800, 400, 200, 50)
        ]

        self.horloge = pygame.time.Clock()
        self.fps = 30

    # Boucle principale
    def main(self):

        # Création des instances de la classe Bouton
        playButton = Button("Jouer", 550, 380, 300, 50, (0, 128, 255))
        creditButton = Button("Crédits", 550, 480, 300, 50, (0, 128, 255))

        # Définition des couleurs
        white: tuple[int, int, int] = (255, 255, 255)
        black: tuple[int, int, int] = (0, 0, 0)

        # 1er niveau
        level1 = Level('Images/EcranAttente.png', self.screen)

        # Définition de la position horizontale de la caméra :
        camera_x = 0

        # Variable pour indiquer si les boutons sont visibles ou non
        main_buttons_visible = True

        level1Ran = False

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Clic sur le bouton Jouer
                    if playButton.x < x < playButton.x + playButton.largeur and playButton.y < y < playButton.y + playButton.hauteur:
                        main_buttons_visible = False
                        # On ne doit plus pouvoir cliquer sur les boutons
                        playButton.erase_button()
                        creditButton.erase_button()
                        level1.run()
                        level1Ran = True

                    # Clic sur le bouton Crédits
                    elif creditButton.x < x < creditButton.x + creditButton.largeur and creditButton.y < y < creditButton.y + creditButton.hauteur:
                        print("Bouton Crédits cliqué")
                        # Ajoutez ici le code pour la fonction "Crédits"

                    # Clic sur la croix de fermeture de fenêtre
                    elif 1400 - closeButtonWidth < x < 1400 and 0 < y < closeButtonHeight:
                        self.running = False

                # Deplacements
                elif level1Ran:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.playerSpeedX = 18

                        if event.key == pygame.K_LEFT:
                            self.playerSpeedX = -18

                        if event.key == pygame.K_UP:
                            self.player.jumped = True
                            self.player.jumpCounter += 1

                        if event.key == pygame.K_SPACE and self.touchGround:
                            if self.gravityDirection == 1:
                                self.gravityDirection = -1
                            else:
                                self.gravityDirection = 1

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.playerSpeedX = 0

                        if event.key == pygame.K_LEFT:
                            self.playerSpeedX = 0

            # Si le niveau est lancé, on fait apparaitre son sol et on gère le déroulement du niveau
            if level1Ran:
                level1.update()

                if self.ground.rect.colliderect(self.player.rect):
                    self.resist = (0, -10)
                    self.touchGround = True
                    self.player.jumpCounter = 0
                else:
                    self.resist = (0, 0)

                for rectangle in self.plateformListRect:
                    platform = Plateform(rectangle)
                    if self.player.rect.midbottom[1] // 10 * 10 == platform.rect.top and self.player.rect.colliderect(
                            rectangle):
                        self.resist = (0, -10)
                        self.player.jumpCounter = 0

                    if self.player.rect.colliderect(platform.rect):
                        dx = self.player.rect.centerx - platform.rect.centerx
                        dy = self.player.rect.centery - platform.rect.centery

                        if dy > 0:
                            self.player.rect.y = (platform.rect.y + platform.rect.h)
                            # Collision en haut de player.rect
                        else:
                            self.player.rect.y = (platform.rect.y - self.player.rect.h)
                            # Collision en bas de player.rect

                    platform.show(self.screen)

                # Dessine le sol
                self.ground.show(self.screen)
                # Le joueur ne peut faire qu'un saut
                if self.player.jumped and self.touchGround:
                    if self.player.jumpCounter < 1:
                        self.player.jump()
                if not self.runningMusic:
                    print("musique")
                    pygame.mixer.init()
                    pygame.mixer.music.load('Musique/musique.mp3')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play(-1)
                    self.runningMusic = True
                # Dessine le player :
                self.player.show(self.screen)
                # Active la gravité
                self.gravityGame()
                self.player.rect.clamp_ip(self.rect)
                self.player.move(self.playerSpeedX)
                pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

            pygame.display.flip()

            # Limite des fps
            self.horloge.tick(self.fps)
            # Dessine les boutons
            if main_buttons_visible:
                playButton.draw(self.screen, white)
                creditButton.draw(self.screen, white)

            # Chargement de l'image de la croix de fermeture
            close_button = pygame.image.load("Images/close_button.png")
            # Redimensionnement de l'image de la croix de fermeture
            closeButtonWidth = 30  # Spécifiez la nouvelle largeur souhaitée
            closeButtonHeight = 30  # Spécifiez la nouvelle hauteur souhaitée
            close_button = pygame.transform.scale(close_button, (closeButtonWidth, closeButtonHeight))

            # Affiche le bouton de fermeture redimensionné en haut à droite
            self.screen.blit(close_button, (1400 - closeButtonWidth, 0))

        # Écran noir
        self.screen.fill(black)

    def gravityGame(self):
        if self.gravityDirection == 1:
            self.player.rect.y += self.gravity[1] + self.resist[1]
        else:
            self.player.rect.y -= self.gravity[1] + self.resist[1]


# Lancement
if __name__ == '__main__':
    pygame.init()
    Game().main()
    pygame.quit()
