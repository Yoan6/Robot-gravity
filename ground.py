import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, startX, startY, width, height):
        super().__init__()
        self.rect = pygame.Rect(startX, startY, width, height)

    def show(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)
