import pygame
from player import Player
import pytmx

class Level:
    def __init__(self, map_path, surface, name_lvl, player):
        self.spawn_x = 10
        self.spawn_y = 100
        self.player = player
        self.name_lvl = name_lvl
        self.display_surface = surface
        map = pygame.image.load(map_path)
        self.zoom = 1
        self.screenWidth = 1700
        self.screenHeight = 900
        self.window = None
        largeur_zoom = int(self.screenWidth * self.zoom)
        hauteur_zoom = int(self.screenHeight * self.zoom)
        self.fond_ecran_zoom = pygame.transform.scale(map, (largeur_zoom, hauteur_zoom))

    def run(self):
        self.window = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.window.blit(self.fond_ecran_zoom, (0, 0))
        pygame.display.set_caption(self.name_lvl)

    def update(self):
        self.window.blit(self.fond_ecran_zoom, (0, 0))

    def spawn(self):
        self.player.rect.x = self.spawn_x
        self.player.rect.y = self.spawn_y