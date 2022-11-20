class Dead(Exception):
    def __init__(self, message):
        super().__init__(message)

class Depression(Exception):
    def __init__(self, message):
        super().__init__(message)

class Poor(Exception):
    def __init__(self, message):
        super().__init__(message)

class Action:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Work:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Rest:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Person:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Здоровье: {self.health}\n' \
               f'Разум: {self.mood}\n' \
               f'Капитал: {self.money}\n'

    def do(self, action):
        self.money = self.money + action.money
        self.health = self.health + action.health
        self.mood = action.mood + self.mood
        if self.mood > 90:
            self.money =+ 5
        if self.health < 40:
            self.mood =- 10
        return Action

    def take_damage(self, health):
        if self.health < 0:
            print("Вы не смогли дожить до следующего дня")
            raise Dead('Вы не смогли дожить до следующего дня')

    def mood(self, mood):
        if self.mood < 0:
            print("Вы сходите с ума от надвигающейся депресии")
            raise Depression('Вы сходите с ума от надвигающейся депресии')

    def money(self, money):
        if self.money < 0:
            print("Вы находитесь в банкротстве")
            raise Poor('Вы находитесь в банкротстве')

    def change_state(self, money, health, mood):
        self.money = self.money + money
        self.health = self.health + health
        self.mood = mood + self.mood