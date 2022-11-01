from character import Character

player1 = Character(name = 'Nikita', health = 100, damage = 2, defence = 0)
print(player1)
player2 = Character(name = 'Arsen', health = 50, damage = 8, defence = 0)
print(player2)
player3 = Character(name = 'Bashi', health = 120, damage = 4, defence = 0)
print(player3)
while True:
    player1.take_damage(-5)
    player1.attack(player2)
    player2.take_damage(-5)
    player2.attack(player3)
    player3.take_damage(-5)
    player3.attack(player1)

    print('-----------------------------------------')
    print(player1)
    print(player2)
    print(player3)