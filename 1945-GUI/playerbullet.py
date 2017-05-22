import pygame

class PlayerBullet:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('resources/bullet.png')

    def run(self):
        self.y -= 13

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))