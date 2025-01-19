import random

class Player:
    def __init__(self, name: str):
        self.name = name
        self.position = 1
        self.turns_to_be_missed = 0
        
    def roll_die(self) -> int:
        dice_roll = random.randint(1, 6)
        return dice_roll