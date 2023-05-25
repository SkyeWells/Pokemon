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
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.menu_image, rect)