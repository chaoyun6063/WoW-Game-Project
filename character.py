from random import randrange


class Character:
    # initialize class
    def __init__(self, character_name, attack_speed = 2, delay = 0):
        self.character_name = character_name
        self.health = 100
        self.attack_speed = attack_speed
        self.delay = delay

    # methods
    def attack(self):
        self.delay = 10 - self.attack_speed

    def is_dead(self):
        return self.health <= 0
    
    def end_round(self):
        self.health = self.health+1 if self.health+1<=100 else 100
        self.delay -= 1

    def print(self):
        print(f"{self.character_name} H:{self.health} D:{self.delay}")
