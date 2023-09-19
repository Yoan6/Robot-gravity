import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, taille):
        super().__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])

    def move(self, speed):
        self.rect.x += speed

    def show(self, surface):
        pygame.draw.rect(surface, (0, 255, 255), self.rect)

