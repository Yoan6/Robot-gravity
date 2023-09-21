import pygame

class Advise(object):
    def __init__(self,x,y,text,height,width):
        self.text=text
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rect = pygame.Rect(x, y, width, height)
        


    def show(self,win,cond): 
        pygame.draw.rect(win, (255,0,0), self.rect, 2)
        if cond:
            self.helping_bubble(win,self.text,(0,0,0),(0,125,255),25)
 

    def helping_bubble(self,screen,text,text_colour,bg_colour,size):
        font = pygame.font.SysFont("Comic Sans",size)
        y_offset = 0
        lines = self.text.split('\n')  # Sépare le texte en lignes sur les sauts de ligne
        text_surface = font.render(self.text,True,text_colour)
        text_rect = text_surface.get_rect(midbottom=self.rect.midtop)
        bg_rect = text_rect.copy()
        bg_rect.inflate_ip(10,10*2)
        frame_rect=bg_rect.copy()
        frame_rect.inflate_ip(4,4)
        pygame.draw.rect(screen,text_colour,frame_rect)
        pygame.draw.rect(screen,bg_colour,bg_rect)
        for line in lines:
            text_surface = font.render(line,True,text_colour)
            text_rect = text_surface.get_rect(midbottom=self.rect.midtop + y_offset)
            screen.blit(text_surface,text_rect)
        
        
        