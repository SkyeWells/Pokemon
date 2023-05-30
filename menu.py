import pygame
import config
import ultilties
import math
from player import Player
from game_state import Gamestate

class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
    def set_up(self):
        self.menu_image = pygame.image.load("Extra/Enterbutton.png")
    def update(self):
        self.screen.fill(config.BLACK)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.menu_image, rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = Gamestate.ENDED
            # handles key events
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game.game_state = Gamestate.ENDED
                    elif event.key == pygame.K_RETURN:
                        self.game.set_up()
                        self.game.game_state = Gamestate.RUNNING