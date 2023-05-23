import pygame
import config
from game_state import Gamestate
#Timestamp 30:34 havent done what he was doing during 30:34
from game import Game
pygame.init()
FPS = 60
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Pokemon Pygame")

game = Game(screen)

game.set_up()

clock = pygame.time.Clock()
while game.game_state == Gamestate.RUNNING:
    clock.tick(60)
    game.update()
    pygame.display.flip()
   