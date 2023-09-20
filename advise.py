import pygame

class Advise(object):
    def __init__(self,x,y,text):
        self.text=text
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y+28, 128, 100)
        


    def show(self,win,cond): 
        pygame.draw.rect(win, (255,0,0), self.rect, 2)
        if cond:
            self.helping_bubble(win,self.text,(0,0,0),(0,125,255),25)
 

    def helping_bubble(self,screen,text,text_colour,bg_colour,size):
        font = pygame.font.SysFont("Comic Sans",size)
        text_surface = font.render(text,True,text_colour)
        text_rect = text_surface.get_rect(midbottom=self.rect.midtop)
        bg_rect = text_rect.copy()
        bg_rect.inflate_ip(10,10)
        frame_rect=bg_rect.copy()
        frame_rect.inflate_ip(4,4)
        pygame.draw.rect(screen,text_colour,frame_rect)
        pygame.draw.rect(screen,bg_colour,bg_rect)
        screen.blit(text_surface,text_rect)