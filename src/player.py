import random

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.position = 1
        self.turns_to_be_missed = 0
        
    def roll_die(self) -> int:
        dice_roll = random.randint(1, 6)
        return dice_roll
    
    def get_current_location(self) -> int:
        return self.position
    
    def move_player(self, move_amount: int) -> None:
        self.position += move_amount
        
    def teleport_player(self, new_location: int) -> None:
        self.position = new_location
        
    def add_turns_to_be_missed(self, amount_rest: int) -> None:
        self.turns_to_be_missed += amount_rest
        
    def spend_turn_to_be_missed(self) -> None:
        self.turns_to_be_missed -= 1
        
    def check_if_turn_missed(self) -> bool:
        return self.turns_to_be_missed > 0