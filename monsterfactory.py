from monster import Monster
import ultilties
import config
import configmonster

class MonsterFactory:
    def __init__(self):
        self.count = 0
    
    def create_monster(self, monster_type):
        random_number = -1
        
        if monster_type == "G":
            random_number = ultilties.generate_random_number(config.GRASS_TYPE_START, config.GRASS_TYPE_START)

        monster = Monster(monster_type, random_number)
        self.count = self.count + 1
        
        return monster