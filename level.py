import pygame
from player import Player
import pytmx

class Level:
    def __init__(self, map_path, surface, name_lvl):
        self.name_lvl = name_lvl
        self.display_surface = surface
        map = pygame.image.load(map_path)
        self.zoom = 1
        screenWidth = 1024  # Spécifiez la largeur souhaitée
        screenHeight = 768  # Spécifiez la hauteur souhaitée
        self.window = pygame.display.set_mode((screenWidth, screenHeight))
        largeur_zoom = int(screenWidth * self.zoom)
        hauteur_zoom = int(screenHeight * self.zoom)
        self.fond_ecran_zoom = pygame.transform.scale(map, (largeur_zoom, hauteur_zoom))

    def run(self):
        self.window.blit(self.fond_ecran_zoom, (0, 0))
        pygame.display.set_caption(self.name_lvl)
        #self.window.blit(self.map, (0, 0))
        #tmx_data = pytmx.util_pygame.load_pygame('maps/TestLevel')

    def update(self):
        self.window.blit(self.fond_ecran_zoom, (0, 0))