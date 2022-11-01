from random import random


class Character:

    def __init__(self, name = '', health = 100, damage = 2, defence = 0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
        self.alive = True

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Здоровье: {self.health}\n' \
               f'Урон: {self.damage}\n' \
               f'Защита: {self.defence}\n'

    def take_damage(self, damage):
        if damage > 0:
            self.health -= max(damage, 0)
    def attack(random, target):
        target.take_damage(random.damage)

def is_alive(self):
    if self.health < 0:
        print('Смерть')
        self.alive = False
    elif self.health > 0:
        print('Продолжаем')
        self.alive = True