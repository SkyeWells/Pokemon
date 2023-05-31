import pygame
import config
import ultilties
import math

class Battle:
    def __init__(self, screen, monster, player):
        self.screen = screen
        self.monster = monster
        self.player = player
    def load(self):
        pass
    
    def render(self):
        self.fill(config.WHITE)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.monster.image, rect)
        pass
    
    def update(self):
        pass