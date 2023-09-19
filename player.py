import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, taille):
        super().__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.jumpStatus = 0
        self.jumpUp = 0
        self.jumpDown = 10
        self.jumped = False
        self.jumpCounter = 0


    def move(self, speed):
        self.rect.x += speed

    def show(self, surface):
        pygame.draw.rect(surface, (0, 255, 255), self.rect)

    def jump(self):
        if self.jumped:
            print(self.jumpDown, self.jumpUp)
            if self.jumpUp >= 10:
                self.jumpDown -= 1
                self.jumpStatus = self.jumpDown

            else:
                self.jumpUp += 1
                self.jumpStatus = self.jumpUp

            if self.jumpDown < 0:
                self.jumpUp = 0
                self.jumpDown = 10
                self.jumped = False

            self.rect.y -= (10 * (self.jumpStatus / 2))
