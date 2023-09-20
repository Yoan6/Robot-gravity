import pygame


class Plateform(pygame.sprite.Sprite):

    def __init__(self, rect):
        super().__init__()
        self.rect = rect

    def show(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), self.rect)
