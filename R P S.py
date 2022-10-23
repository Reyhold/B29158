import random

def game(choice, result):
    print("")
    print("=====Start Game rock, paper,  scissors=====")
    computer_choice = random.choice("rps")
    print("--------------------------------")
    print("Your select – ", str.capitalize(choice))
    print("Computer select —", str.capitalize(computer_choice))