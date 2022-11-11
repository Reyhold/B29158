from lessom.character import Character
import random

class Ninja(Character):
    max_health = 100

    def __init__(self, name='', health=100, damage=1, dodge=0):
        Character.__init__(self, name, health, damage, dodge)
        self.dodge = dodge



    def take_damage(self, damage):
        if self.dodge_success():
            return "Уворот"
        self.health -= damage
        return f"{self.name} получил {damage} урона"  #честно, вот эта строка была найдена в интернете, остальное я нашел в записи урока

    def dodge_success(self):
        dodge_chance = self.dodge * 5
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_chance:
            return True
        return False