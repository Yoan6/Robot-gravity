import pygame
from player import Player

class Level:
    def __init__(self, map_path, surface):
        self.display_surface = surface
        map = pygame.image.load(map_path)
        windowWidth = 1400  # Spécifiez la largeur souhaitée
        windowHeight = 900  # Spécifiez la hauteur souhaitée
        self.window = pygame.display.set_mode((windowWidth, windowHeight))
        self.map = pygame.transform.scale(map, (windowWidth, windowHeight))

    def run(self):
        print("Level 1 en cours")
        self.window.blit(self.map, (0, 0))