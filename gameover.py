import pygame

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
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
            game_over_text = self.font.render("Game Over", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(game_over_text, text_rect)