import items
import characters
import monsters

meat = weak_meat()
ali = warrior()
ali.health = 20
meat.eat(ali)
print(ali.health)
