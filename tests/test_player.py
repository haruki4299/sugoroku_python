import pytest
from src.player import Player

def test_player_name():
    player = Player("Haruki")
    assert player.name == "Haruki"