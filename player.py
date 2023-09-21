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
        self.jumpDown = 5
        self.jumped = False
        self.jumpCounter = 0
        self.walkRight = [pygame.image.load('Images/SpriteRobot/Head.png'), pygame.image.load('Images/SpriteRobot/Head2.png'), pygame.image.load('Images/SpriteRobot/Head3.png'), pygame.image.load('Images/SpriteRobot/Head4.png')]
        self.walkLeft = [pygame.image.load('Images/SpriteRobot/Head.png'), pygame.image.load('Images/SpriteRobot/Head4.png'), pygame.image.load('Images/SpriteRobot/Head3.png'), pygame.image.load('Images/SpriteRobot/Head2.png')]
        self.char = pygame.image.load('Images/SpriteRobot/Head.png')



    def move(self, speed):
        self.rect.x += speed

    def show(self, surface,right,left,walkCount,x,y):
        if right:
            surface.blit(self.walkRight[walkCount//4], (self.rect.x,self.rect.y))
        elif left:
            surface.blit(self.walkLeft[walkCount//4], (self.rect.x,self.rect.y))
        else:
            surface.blit(self.char, (self.rect.x,self.rect.y))

    def jump(self):
        if self.jumped:
            if self.jumpUp >= 8:
                self.jumpDown -= 1
                self.jumpStatus = self.jumpDown

            else:
                self.jumpUp += 1
                self.jumpStatus = self.jumpUp

            if self.jumpDown < 0:
                self.jumpUp = 0
                self.jumpDown = 5
                self.jumped = False

            self.rect.y -= (10 * (self.jumpStatus / 2))