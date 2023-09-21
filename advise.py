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
        if cond:
            self.helping_bubble(win,self.text,(255,255,255),25)
 

    def helping_bubble(self,screen,text,text_colour,size):
        font = pygame.font.SysFont("Comic Sans",size)
        y_offset = 0
        lines = self.text.split('\n')  # Sépare le texte en lignes sur les sauts de ligne      
        for line in lines:
            texte_surface = font.render(line, True, text_colour)
            texte_rect = texte_surface.get_rect()
            texte_rect.center = (self.x + self.width / 2, self.y - 100 + self.height / 2 + y_offset)
            screen.blit(texte_surface, texte_rect)
            y_offset += 25  # Espacement vertical entre les lignes
        
        
        