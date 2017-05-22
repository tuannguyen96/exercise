import pygame

from gamemanager import *
from inputManager import *
from player import *
from background import *
from enemy import *

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption('1945 Strikers - Remade by Techkids')
    return screen

def run():
    game_manager.run()

def draw(screen):
    screen.fill((0,0,0))
    game_manager.draw(screen)

screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
game_manager.add(Player())
game_manager.add(Enemy_type_1(300,0))
game_manager.add(Enemy_type_2(0,0))

loop = True

player = Player()
background = Background()
enemy_type_1 = Enemy_type_1(300, 0)
enemy_type_2 = Enemy_type_2(-50,-50)

while loop:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    #UPDATE LOGIC

    run()

    input_manager.run(events)

    # UPDATE GRAPHICS

    draw(screen)

    # DELAY BY FRAME RATE

    pygame.display.flip()
    clock.tick(60)

pygame.quit()