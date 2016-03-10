import items

class human:
    def __init__(self, name):
        self.name = name        
        self.level = 1
        self.max_experience = 100
        
        self.wearable_items = {
        'helmet': None,
        'chest': None,
        'arm:': None,
        'shoe': None,
        }
        
        self.items = {
        'elixirs': None,
        'wearable': wearable_items,
        'mounts': None,
                'coins': None,
                'junk': None,
                'food': None,
                'quest_item': None,
        }
        
        self.abilities = {
        'movement': basic_movement,
        'proffesion': None,
        'special_acts': None
        }
        
        self.skills={
        '1': punch,
        '2': None,
        '3': None,
        '4': None
        }
    
    def level_up(level, experience, max_experience):
        if experience >= max_experience:
            level += 1
            max_experience *= 1.25
            experience = 0
        return [level, experience, max_experience]
    
    def earn_experience(experience, level, monster_level):
        experience += level*(2/3)**(level-monster_level)
        return experience
        

class warrior(human):
    def __init__(self):
                self.max_health = 165
                self.health = 165
                self.power = 8
                self.block = 10
                self.life_steal = 2
                self.skills['2']= 'warrior_scream'
        
        
class mage(human):
    def __init__(self):
        self.health = 110
        self.power = 15
        self.block = 2
        self.life_steal = 0
        self.skills['2']= 'rage_of_mage'
