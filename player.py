import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, height):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.height[0], self.height[1])

    def show(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
