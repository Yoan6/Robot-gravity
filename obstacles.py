import pygame

class Spike(object):
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x, y, width, height)
        


    def show(self,win): 
        pygame.draw.rect(win, (255,0,0), self.rect, 2)