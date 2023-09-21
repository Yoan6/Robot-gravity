import pygame


class GameOver:
    def __init__(self, screen):
        self.screen = screen
        image = pygame.image.load("Images/gameover.jpg")
        self.image = pygame.transform.scale(image, (1700, 900))
        self.image_rect = self.image.get_rect()
        self.show_window = False
        self.show_time = 0

    def show(self):
        self.show_window = True
        self.show_time = pygame.time.get_ticks()

    def update(self):
        if self.show_window:
            current_time = pygame.time.get_ticks()
            if current_time - self.show_time >= 5000:
                self.show_window = False

    def draw(self):
        if self.show_window:
            self.screen.blit(self.image, self.image_rect)

