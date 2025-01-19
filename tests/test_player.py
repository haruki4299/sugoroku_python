import pytest
from src.player import Player

def test_player_creation():
    player = Player("Haruki")
    assert player.name == "Haruki"

@pytest.mark.parametrize("roll", range(100))
def test_dice_roll():
    player = Player("Haruki")
    dice_roll = player.roll_die()
    assert 1 <= dice_roll <= 6, f"Dice roll {dice_roll} is out of range"
    assert isinstance(dice_roll, int), f"Dice roll {dice_roll} is not an integer"