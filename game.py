import pygame
import config
import ultilties
import math
from player import Player
from game_state import Gamestate, CurrentGameState
from monsterfactory import MonsterFactory
from game_view.map import Map
from game_view.battle import Battle

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = Gamestate.NONE
        self.player_has_moved = False
        self.monster_factory = MonsterFactory()
        self.map = Map(screen)
        self.battle = None
        
    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("do set up")
        self.current_game_state = CurrentGameState.MAP
        
        self.map.load("01")
        
    def update(self):
        if self.game_state == CurrentGameState.MAP:
            self.player_has_moved = False
            self.screen.fill(config.BLACK)
            self.handle_events()
            
            self.map.render(self.screen, self.player, self.objects)
                
            if self.player_has_moved:
                self.determine_player_actions()
        elif self.current_game_state == CurrentGameState.BATTLE:
            self.battle.update()
            self.battle.render()
        
            
        
    def determine_player_actions(self):
        map_tile = self.map.map_array[self.player.position[1]][ self.player.position[0]]
        print(map_tile)
        
        if map_tile == config.MAP_TILE_TILE:
            return
        
        self.determine_pokemon_found(map_tile)
    
    def determine_pokemon_found(self, map_tile):
        random_number = ultilties.generate_random_number(1, 10)
        # 20 percent chance of getting a pokemon
        if random_number <= 2:
            found_monster = self.monster_factory.create_monster(map_tile)
            print("you found a monster!")
            print("monser type: " + found_monster.type)
            print("attack: " + str(found_monster.attack))
            print("health: " + str(found_monster.health))
            
            self.battle = Battle(self.screen, found_monster, self.player)
            self.current_game_state = CurrentGameState.BATTLE
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = Gamestate.ENDED
            # handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = Gamestate.NONE
                elif event.key == pygame.K_w:
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s:
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a:
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d:
                    self.move_unit(self.player, [1, 0])

    def move_unit(self, unit, position_change):
        self.player_has_moved = False
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return
        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return
        
        if self.map.map_array[new_position[1]][new_position[0]] == config.MAP_TILE_WATER:
            return
        
        self.player_has_moved = True
        
        unit.update_position(new_position)
