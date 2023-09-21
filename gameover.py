import pygame

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        image = pygame.image.load("Images/gameover.jpg")
        self.image = pygame.transform.scale(image, (1024, 768))
        self.image_rect = self.image.get_rect()
        self.show_window = False
        self.timer = 0

    def show(self):
        self.show_window = True
        self.timer = pygame.time.get_ticks()

    def update(self):
        if self.show_window:
            current_time = pygame.time.get_ticks()
            if current_time - self.timer >= 5000:  # Affiche la fenêtre pendant 5 secondes
                self.show_window = False

    def draw(self):
        if self.show_window:
            # Affichez l'image à la position souhaitée (par exemple, au centre de l'écran)
            self.screen.blit(self.image, self.image_rect)
