import pygame
import config
from game_state import Gamestate
from menu import Menu
#Timestamp 11:52 5th vid
from game import Game
pygame.init()
FPS = 60
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Pokemon Pygame")

game = Game(screen)
game.set_up()

menu = Menu(screen, game)
menu.set_up()

clock = pygame.time.Clock()
while game.game_state != Gamestate.ENDED:
    if game.game_state == Gamestate.NONE:
        menu.update()
    if game.game_state == Gamestate.RUNNING:
        game.update()
    clock.tick(60)
    game.update()
    pygame.display.flip()
   