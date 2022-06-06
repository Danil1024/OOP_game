from settings import *
from random import randint
from exceptions import *


class Player:
    def __init__(self, name):
        self.name = name
        self.lives = LIVES
        self.score = 0
        self.allowed_attacks = HEROES 

    @staticmethod
    def fight(attack, defense):
        return(ACTION_RESULT[attack, defense])

    def decrease_lives(self):
        self.lives -= 1
        print(f"You have {self.lives} lives left\n")
        if self.lives < 1:
            print(f"You scored: {self.score}")
            raise GameOver()

    def attack(self, enemy_obj):
        chosen_attack = input('select an attacker: ')
        while chosen_attack not in self.allowed_attacks:
            for num, name in self.allowed_attacks.items():
                print(num, name)
            chosen_attack = input('select an attacker: ')
        chosen_attack = self.allowed_attacks[chosen_attack]
        result_fight = self.fight(chosen_attack, enemy_obj.select_attack())
        if result_fight == 1:
            print('You attacked successfully!')
            enemy_obj.decrease_lives()
            self.score += 1
        elif result_fight == -1:
            print('You missed!')
        else:
            print("It's a draw!")

    def defence(self, enemy_obj):
        chosen_protection = input('choose protection: ')
        while chosen_protection not in self.allowed_attacks:
            for num, name in self.allowed_attacks.items():
                print(num, name)
            chosen_protection = input('choose protection: ')
        chosen_protection = self.allowed_attacks[chosen_protection]
        result_fight = self.fight(enemy_obj.select_attack(), chosen_protection)
        if result_fight == 1:
            print('Enemy hit')
            self.decrease_lives()
        elif result_fight == -1:
            print('Enemy missed!')
        else:
            print("It's a draw!")


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        return HEROES[str(randint(1, 3))]

    def decrease_lives(self):
        self.lives -= 1
        if self.lives < 1:
            raise EnemyDown()
        print(f'Enemy lives = {self.lives}')
