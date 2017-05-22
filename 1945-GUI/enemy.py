import pygame

class Enemy_type_1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/enemy_plane_white_1.png')

    def run(self):
        self.y += 8

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Enemy_type_2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('resources/enemy-green-1.png')

    def run(self):
        self.y += 7
        self.x += 7

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))