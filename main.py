import pygame
import sys
import pytmx
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
        self.player_x = 400
        self.player_y = 400
        self.playerSpeedX = 0
        self.taille = [32, 64]
        self.player = Player(self.player_x, self.player_y, self.taille)
        self.ground = Ground()
        self.gravity = (0, 10)
        self.resist = (0, 0)
        self.touchGround = False
        self.rect = pygame.Rect(0, 0, 1400, 900)

        # 1 = vers le bas, autre = vers le haut
        self.gravityDirection = 1

    # Boucle principale
    def main(self):

        # Création des instances de la classe Bouton
        playButton = Button("Jouer", 550, 380, 300, 50, (0, 128, 255))
        creditButton = Button("Crédits", 550, 480, 300, 50, (0, 128, 255))

        # Définition des couleurs
        white: tuple[int, int, int] = (255, 255, 255)
        black: tuple[int, int, int] = (0, 0, 0)

        timer = pygame.time.Clock()

        # Variable de jeux
        scroll_left = False
        scroll_right = False
        scroll = 0
        scroll_speed = 1

        if scroll_left == True:
            scroll -= 5
        if scroll_right == True:
            scroll += 5

        # 1er niveau
        level1 = Level('Images/farm.png', self.screen)

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

                        if event.key == pygame.K_SPACE:
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
                if self.ground.rect.colliderect(self.player.rect):
                    # Si le personnage collisionne par le bas, la résistance doit se faire vers le bas, sinon vers le haut
                    if self.ground.rect.y > self.player.y:
                        self.resist = (0, -10)
                    else:
                        self.resist = (0, 10)

                    self.touchGround = True
                    self.player.jumpCounter = 0

                else:
                    self.resist = (0, 0)

                level1.update()
                # Le joueur ne peut faire qu'un saut
                if self.player.jumped and self.touchGround:
                    if self.player.jumpCounter < 1:
                        self.player.jump()

                # Dessine le player :
                self.player.show(self.screen)
                # Dessine le sol
                self.ground.show(self.screen)
                # Active la gravité
                self.gravityGame()
                self.player.rect.clamp_ip(self.rect)
                self.player.move(self.playerSpeedX)
                pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

            pygame.display.flip()

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

            # On défini un laps de temps de 60 images par seconde par game loop
            timer.tick(60)

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
