import pygame
import config
from game_state import Gamestate
from menu import Menu
#Timestamp 52:19 5th vid
#6th vid link: https://www.youtube.com/watch?v=5dgAxPRSNnE
#program is crashing.
from game import Game
pygame.init()
FPS = 60
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Pokemon Pygame")

game = Game(screen)

menu = Menu(screen, game)
menu.set_up()

clock = pygame.time.Clock()
while game.game_state != Gamestate.ENDED:
    clock.tick(50)
    
    if game.game_state == Gamestate.NONE:
        menu.update()

    if game.game_state == Gamestate.RUNNING:
        game.update()

    pygame.display.flip()
   