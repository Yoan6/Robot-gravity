import pygame
import sys
import pytmx
from pygame.sprite import Group

import obstacles
from button import Button
from player import *
from player import Player
from level import Level
from obstacles import Spike
from advise import Advise
from plateform import Plateform
from gameover import *
from PartRecup import Arms
from win import Win


class Game:

    def __init__(self):
        # Configuration de la taille de la fenêtre
        self.screen_width = 1700
        self.screen_height = 900
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Page d'accueil")
        self.running = True
        self.player_x = 380
        self.player_y = 400
        self.playerSpeedX = 0
        self.right = False
        self.left = False
        self.gravityI = False
        self.gravityInv = False
        self.walkCount = 0
        self.taille = [32, 60]
        self.player = Player(self.player_x, self.player_y, self.taille, 10)
        self.gravity = (0, 20)
        self.resist = (0, 0)
        self.runningMusic = False
        self.gameover = GameOver(self.screen)
        self.win = Win(self.screen)
        self.rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.wincond = Arms(1660, 220)
        self.arms = True

        # 1 = vers le bas, autre = vers le haut
        self.gravityDirection = 1
        self.plateformListRect = [
            pygame.Rect(0, 500, 175, 400),
            pygame.Rect(15, 270, 225, 30),
            pygame.Rect(260, 0, 275, 90),
            pygame.Rect(450, 240, 100, 60),
            pygame.Rect(450, 690, 125, 350),
            pygame.Rect(600, 360, 100, 60),
            pygame.Rect(750, 570, 100, 400),
            pygame.Rect(925, 0, 100, 120),
            pygame.Rect(1005, 390, 90, 25),
            pygame.Rect(1170, 0, 120, 150),
            pygame.Rect(1170, 570, 100, 400),
            pygame.Rect(1360, 0, 80, 150),
            pygame.Rect(1340, 570, 135, 25),
            pygame.Rect(1512, 0, 275, 150),
            pygame.Rect(1605, 150, 100, 35),
            pygame.Rect(1650, 185, 50, 30),
            pygame.Rect(1590, 775, 150, 200)

        ]

        self.objectPic = [
            #Spike(0,490,170,25),
            #Spike(1000,110,20,25),
            #Spike(454,670,115,25),
            #Spike(1000,370,20,25),
            #Spike(1080,370,20,25),
            #Spike(1170,545,40,25),
            #Spike(1265,142,20,25),
            #Spike(1415,142,20,25),
            #Spike(1587,762,170,25)
        ]

        self.objectAdv = [
            
            #Advise(210,200,"Un jour fut née un Grand sage. \n Sa Phrase préférée? Fuck Yoan.",100,10)
        ]


        self.horloge = pygame.time.Clock()
        self.fps = 30

    # Boucle principale
    def main(self):
        Starting_background = pygame.image.load("Images/EcranAttente.png")
        Starting_background =  pygame.transform.scale(Starting_background, (self.screen_width,self.screen_height))
        self.screen.blit(Starting_background,(0,0))
        # Création des instances de la classe Bouton
        playButton = Button("Jouer", 700, 420, 300, 50, (0, 128, 255))
        creditButton = Button("Crédits", 700, 520, 300, 50, (0, 128, 255))
        # Définition des couleurs
        white: tuple[int, int, int] = (255, 255, 255)
        black: tuple[int, int, int] = (0, 0, 0)

        # 1er niveau
        level1 = Level('maps/Level1.png', self.screen, "Niveau 1", self.player)
        # 2ème niveau
        level2 = Level('maps/Level2.png', self.screen, "Niveau 2", self.player)
        # 3ème niveau
        level3 = Level('maps/Level3.png', self.screen, "Niveau 3", self.player)
        level2.spawn()

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
                        level2.run()
                        level2.draw_life()
                        level1Ran = True

                    # Clic sur le bouton Crédits
                    elif creditButton.x < x < creditButton.x + creditButton.largeur and creditButton.y < y < creditButton.y + creditButton.hauteur:
                        self.screen.fill("black")
                        creditRan = True
                        playButton.erase_button()
                        creditButton.erase_button()


                # Deplacements
                elif level1Ran:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            self.playerSpeedX = 10
                            self.right = True
                            self.left = False

                        elif event.key == pygame.K_LEFT:
                            self.playerSpeedX = -10
                            self.left = True
                            self.right = False

                        if event.key == pygame.K_UP:
                            self.player.jumped = True
                            self.player.jumpCounter += 1

                        # Inversion de la gravité si on peut (gravityI)
                        if event.key == pygame.K_SPACE:
                            if self.gravityDirection == 1 and self.gravityI:
                                self.gravityDirection = -1
                                self.gravityInv = True
                            elif self.gravityI:
                                self.gravityDirection = 1
                                self.gravityInv = False

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            self.playerSpeedX = 0
                            self.right = False

                        if event.key == pygame.K_LEFT:
                            self.playerSpeedX = 0
                            self.left = False

            # Si le niveau est lancé, on fait apparaitre son sol et on gère le déroulement du niveau
            if level1Ran:              
                level2.update()
                level2.draw_life()
                self.gravityI = False

                self.resist = (0, 0)

                for rectangle in self.plateformListRect:
                    platform = Plateform(rectangle)
                    if self.player.rect.midbottom[1] // 10 * 10 == platform.rect.top and self.player.rect.colliderect(
                            rectangle):
                        self.resist = (0, -10)

                    if self.wincond.rect.colliderect(self.player.rect) :
                        self.arms = False
                        self.win.show()
                        self.win.update()
                        self.win.draw()

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

                    # platform.show(self.screen)
                    if self.arms :
                        self.wincond.show(self.screen)

                for pic in self.objectPic:
                    if self.player.rect.colliderect(pic):
                        self.player.nb_life=self.player.nb_life-1
                        level2.spawn()
                        # La gravité doit forcément être vers le bas :
                        self.gravityDirection = 1
                        self.gravityInv = False

                        if self.player.nb_life==0:
                            self.gameover.show()
                            self.gameover.update()
                            self.gameover.draw()

                            pygame.time.wait(500)
                            pygame.quit()



                    # pic.show(self.screen)

                ShowBubble=False
                for adv in self.objectAdv:
                    if self.player.rect.colliderect(adv):
                        ShowBubble=True
                    adv.show(self.screen,ShowBubble)
                    ShowBubble=False


                # Le joueur ne peut faire qu'un saut
                if self.player.jumped:
                    if self.player.jumpCounter < 1:
                        self.player.jump()
                if not self.runningMusic:
                    pygame.mixer.init()
                    pygame.mixer.music.load('Musique/musique.mp3')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                    self.runningMusic = True
                # Dessine le player :
                if self.walkCount < 15:
                    self.walkCount = self.walkCount + 1
                else:
                    self.walkCount = 0
                self.player.show(self.screen, self.right, self.left, self.walkCount, self.gravityInv)

                # Active la gravité
                self.gravityGame()
                self.player.move(self.playerSpeedX)

                # Si le joueur sort de la map, il revient au spawn et perd une vie
                if not self.player.rect.colliderect(self.rect):
                    
                    level2.spawn()
                    # La gravité doit forcément être vers le bas :
                    self.gravityDirection = 1
                    self.gravityInv = False

                    # Réduction de vie :
                    self.player.nb_life=self.player.nb_life-1

                if self.player.nb_life<=0:
                    self.gameover.show()
                    self.gameover.update()
                    self.gameover.draw()
                    print("Première condition")

                if self.player.nb_life<0:
                    pygame.time.wait(2000)
                    pygame.quit()
                    print("Deuxième condition")



            # Affiche les crédits
            elif creditRan:
                credits = pygame.image.load("Images/credits.png")
                image_credits = pygame.transform.scale(credits, (self.screen_width, self.screen_height))
                self.screen.blit(image_credits, (0,0))
            pygame.display.flip()

            # Limite des fps
            self.horloge.tick(self.fps)
            # Dessine les boutons
            if main_buttons_visible:
                playButton.draw(self.screen, white)
                creditButton.draw(self.screen, white)

            

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
