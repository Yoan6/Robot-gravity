import pygame

class Arms(object):
    def __init__(self,x,y):
        self.img = pygame.image.load('Images/SpriteRobot/Arms.png')
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 40, 31)
        


    def show(self,win): 
        #Décommenter la ligne d'en dessous pour voir la hitbox
        #pygame.draw.rect(win, (255,0,0), self.rect, 2)
        win.blit(self.img, (self.x,self.y))