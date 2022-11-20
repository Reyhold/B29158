from car import Person
from car import Action
from car import Work
from car import Rest

import random

person = Person(name='Витя', health=100, mood=100, money=0)
go_to_park = Rest(name = 'Сходить в парк', health=3, mood=15, money=0)
go_to_factory = Work(name = 'Пойти на завод', money = 50, mood = -10, health = -3)
go_to_hospital = Action(name = 'Пойти в больницу', money = -20, mood = -5, health = 20)




print(person)

person.change_state(money = random.randint(20, 100),
                    mood = random.randint(-20, -10),
                    health = random.randint(-10, -5))

print(person)
person.do(go_to_park)
print("Вы прошлись по парку и восстановились")
print(person)

person.do(go_to_factory)
print("Вы работали на заводе и получили свою дневную зарплату")

print(type(go_to_factory) == Work)

print(person)

person.do(go_to_hospital)
print("Вы зашли в поликлинику")
print(type(go_to_hospital) == Work)
print(person)

