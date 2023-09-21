import pygame

class Arms(object):
    def __init__(self,x,y):
        self.img = pygame.image.load('Images/SpriteRobot/Arms.png')
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 40, 31)
        


    def show(self,win):
        win.blit(self.img, (self.x,self.y))