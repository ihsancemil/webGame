import characters

class food:
    def eat(self, character):
        character.health += self.healing
        if character.max_health < character.health:
            character.health = character.max_health
        

class weak_meat(food):
    def __init__(self):
        self.healing = 5


