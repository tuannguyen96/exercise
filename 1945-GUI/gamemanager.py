import pygame

class GameManager:
    def __init__(self):
        self.game_objects = []

    def add(self, game_objects):
        self.game_objects.append(game_objects)

    def run(self):
        for game_objects in self.game_objects:
            game_objects.run()

    def draw(self,screen):
        for game_objects in self.game_objects:
            game_objects.draw(screen)

game_manager = GameManager()
