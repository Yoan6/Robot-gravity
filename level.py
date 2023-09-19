import pygame
from player import Player


class Level:
    def __init__(self, map_path, surface):
        self.display_surface = surface
        map = pygame.image.load(map_path)
        screenWidth = 1400  # Spécifiez la largeur souhaitée
        screenHeight = 900  # Spécifiez la hauteur souhaitée
        self.window = pygame.display.set_mode((screenWidth, screenHeight))
        self.map = pygame.transform.scale(map, (screenWidth, screenHeight))

    def run(self):
        self.window.blit(self.map, (0, 0))

    def update(self):
        self.window.blit(self.map, (0, 0))