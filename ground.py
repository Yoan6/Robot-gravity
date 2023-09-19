import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 600, 1400, 900)

    def show(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)
