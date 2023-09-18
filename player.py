import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, width, height):
        super().__init__()
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = [0, 0]  # La vitesse initiale du sprite

    def update(self):
    # Permet de mettre à jour le sprite du robot à chaque game loop

        global camera_x