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
        self.walkRight = [pygame.image.load('Images/SpriteRobot/WalkingLegs11.png'),
                          pygame.image.load('Images/SpriteRobot/WalkingLegs21.png')]
        self.walkLeft = [pygame.image.load('Images/SpriteRobot/WalkingLegs12.png'),
                         pygame.image.load('Images/SpriteRobot/WalkingLegs22.png')]
        self.walkRightI = [pygame.image.load('Images/SpriteRobot/WalkingLegsInversed11.png'),
                           pygame.image.load('Images/SpriteRobot/WalkingLegsInversed21.png')]
        self.walkLeftI = [pygame.image.load('Images/SpriteRobot/WalkingLegsInversed12.png'),
                          pygame.image.load('Images/SpriteRobot/WalkingLegsInversed22.png')]
        self.char = pygame.image.load('Images/SpriteRobot/StandingWithouArms.png')
        self.charI = pygame.image.load('Images/SpriteRobot/StandingWithouArmsInverse.png')

    def move(self, speed):
        self.rect.x += speed

    def show(self, surface, right, left, walkCount, gravity):
        if gravity:
            if right:
                surface.blit(self.walkRightI[walkCount // 8], (self.rect.x, self.rect.y))
            elif left:
                surface.blit(self.walkLeftI[walkCount // 8], (self.rect.x, self.rect.y))
            else:
                surface.blit(self.charI, (self.rect.x, self.rect.y))
        else:
            if right:
                surface.blit(self.walkRight[walkCount // 8], (self.rect.x, self.rect.y))
            elif left:
                surface.blit(self.walkLeft[walkCount // 8], (self.rect.x, self.rect.y))
            else:
                surface.blit(self.char, (self.rect.x, self.rect.y))

    # Fonction sauter
    def jump(self, gravity):
        if self.jumped:
            if self.jumpUp >= 12:
                self.jumpDown -= 1
                self.jumpStatus = self.jumpDown

            else:
                self.jumpUp += 1
                self.jumpStatus = self.jumpUp

            if self.jumpDown < 0:
                self.jumpUp = 0
                self.jumpDown = 5
                self.jumped = False

            if gravity == 1:
                self.rect.y -= (10 * (self.jumpStatus / 2))
            else:
                self.rect.y += (10 * (self.jumpStatus / 2))
