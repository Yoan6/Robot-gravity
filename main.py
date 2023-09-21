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
from gameover import *


class Game:

    def __init__(self):
        # Configuration de la taille de la fenêtre
        self.screen_width = 1024
        self.screen_height = 768
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Page d'accueil")
        self.running = True
        self.player_x = 380
        self.player_y = 400
        self.playerSpeedX = 0
        self.right = False
        self.left = False
        self.gravityI = False
        self.walkCount = 0
        self.taille = [128, 128]
        self.player = Player(self.player_x, self.player_y, self.taille)
        self.ground = Ground(0, 767, self.screen_width, self.screen_height)
        self.gravity = (0, 10)
        self.resist = (0, 0)
        self.touchGround = False
        self.runningMusic = False
        self.rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)

        # 1 = vers le bas, autre = vers le haut
        self.gravityDirection = 1
        self.plateformListRect = [
            pygame.Rect(300, 500, 100, 50),
            pygame.Rect(800, 400, 200, 50),
            pygame.Rect(800, 600, 200, 50)
        ]

        self.horloge = pygame.time.Clock()
        self.fps = 30

    # Boucle principale
    def main(self):

        # Création des instances de la classe Bouton
        playButton = Button("Jouer", 360, 320, 300, 50, (0, 128, 255))
        creditButton = Button("Crédits", 360, 420, 300, 50, (0, 128, 255))
        # Définition des couleurs
        white: tuple[int, int, int] = (255, 255, 255)
        black: tuple[int, int, int] = (0, 0, 0)

        # 1er niveau
        level1 = Level('maps/Level1.png', self.screen, "Niveau 1")
        # 2ème niveau
        level2 = Level('maps/Level2.png', self.screen, "Niveau 2")
        # 3ème niveau
        level3 = Level('maps/Level3.png', self.screen, "Niveau 3")

        # Variable pour indiquer si les boutons sont visibles ou non
        main_buttons_visible = True

        level1Ran = False
        creditRan = False

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
                        level3.run()
                        level1Ran = True

                    # Clic sur le bouton Crédits
                    elif creditButton.x < x < creditButton.x + creditButton.largeur and creditButton.y < y < creditButton.y + creditButton.hauteur:
                        self.screen.fill("black")
                        creditRan = True
                        playButton.erase_button()
                        creditButton.erase_button()

                    # Clic sur la croix de fermeture de fenêtre
                    elif self.screen_width - closeButtonWidth < x < self.screen_width and 0 < y < closeButtonHeight:
                        self.running = False

                # Deplacements
                elif level1Ran:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.playerSpeedX = 18
                            self.right = True
                            self.left = False

                        elif event.key == pygame.K_LEFT:
                            self.playerSpeedX = -18
                            self.left = True
                            self.right = False

                        if event.key == pygame.K_UP:
                            self.player.jumped = True
                            self.player.jumpCounter += 1

                        # Inversion de la gravité si on peut (gravityI)
                        if event.key == pygame.K_SPACE and self.touchGround:
                            if self.gravityDirection == 1 and self.gravityI:
                                self.gravityDirection = -1
                            elif self.gravityI:
                                self.gravityDirection = 1

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.playerSpeedX = 0
                            self.right = False

                        if event.key == pygame.K_LEFT:
                            self.playerSpeedX = 0
                            self.left = False

            # Si le niveau est lancé, on fait apparaitre son sol et on gère le déroulement du niveau
            if level1Ran:
                level3.update()
                self.gravityI = False
                if self.ground.rect.colliderect(self.player.rect):
                    self.resist = (0, -10)
                    self.touchGround = True
                    self.player.jumpCounter = 0
                    self.gravityI = True
                else:
                    self.resist = (0, 0)

                for rectangle in self.plateformListRect:
                    platform = Plateform(rectangle)
                    if self.player.rect.midbottom[1] // 10 * 10 == platform.rect.top and self.player.rect.colliderect(
                            rectangle):
                        self.resist = (0, -10)

                    if self.player.rect.colliderect(platform.rect):
                        dx = self.player.rect.centerx - platform.rect.centerx
                        dy = self.player.rect.centery - platform.rect.centery
                        self.gravityI = True

                        if dy > 0:
                            self.player.rect.y = (platform.rect.y + platform.rect.h)
                            # Collision en haut de player.rect
                        else:
                            self.player.rect.y = (platform.rect.y - self.player.rect.h)
                            self.player.jumpCounter = 0
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
                if self.walkCount < 15:
                    self.walkCount = self.walkCount + 1
                else:
                    self.walkCount = 0
                self.player.show(self.screen, self.right, self.left, self.walkCount, self.player_x, self.player_y)

                # Active la gravité
                self.gravityGame()
                self.player.rect.clamp_ip(self.rect)
                self.player.move(self.playerSpeedX)
                pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

            elif creditRan:
                credits = Button("Développé par : \n - Yoan Delannoy \n - Aurèle Dunand \n\n Musique et effets sonores : \n - Esteban Elias Pueyo \n - Musique venant de ... \n\n Éléments graphiques, visuel \n - Esteban Elias Pueyo \n - Thommas Boussit - Principal graphiste", 0, 0, self.screen_width, self.screen_height, black)
                credits.draw(self.screen, white)
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
            self.screen.blit(close_button, (self.screen_width - closeButtonWidth, 0))

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
