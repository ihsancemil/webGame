import random
import items

class root_of_monsters:
    def item_drop(self):
        rand = random.randrange(1,1000,1)
        dropped_list=[]
        
        for queue in self.drop_list:
            if rand%queue[0] == 0:
                dropped_list.append(queue)
        return dropped_list

class duck(root_of_monsters):
    def __init__(self):
        self.name = "duck"
        self.health = 45
        self.power = 4
        self.monster_level = 1

        #drop_rate, type, name
        self.drop_list = [
        [5, 'food', 'weak_meat'],
        [13, 'coins', 'duck_coin'],
        [47, 'wearable', 'old_maul'],
        [49, 'wearable', 'old_staff'],
        [3, 'junk', 'dirth']
        ]


class wild_bear(root_of_monsters):
    def __init__(self):
        self.name = "wild_bear"
        self.health = 60
        self.power = 6
        self.monster_level = 1

        #drop_rate, type, name
        self.drop_list = [
        [5, 'food', 'weak_meat'],
        [13, 'coins', 'wild_coin'],
        [43, 'wearable', 'old_maul'],
        [41, 'wearable', 'old_staff'],
        [3, 'junk', 'dirth'],
        [4, 'elixir', 'weak_potion']
        ]

first = duck()
print(first.item_drop())
