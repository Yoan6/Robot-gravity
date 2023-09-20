import pygame

class Spike(object):
    def __init__(self,x,y):
        self.img = pygame.image.load('Images/Spikes.png')
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y+28, 128, 100)
        


    def show(self,win): 
        pygame.draw.rect(win, (255,0,0), self.rect, 2)
        win.blit(self.img, (self.x,self.y))