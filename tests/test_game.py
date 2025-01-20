import pytest

from src.board import Board
from src.game import Game
from src.player import Player
import src.utils as utils

def test_adding_player_to_game():
    game = Game()
    assert len(game.players) == 0
    new_player = Player("A")
    game.add_player(new_player)
    assert len(game.players) == 1
    new_player = Player("B")
    game.add_player(new_player)
    assert len(game.players) == 2
    
    assert game.players[0].name == "A"
    assert game.players[1].name == "B"
    
def test_set_up_players(monkeypatch):
    # Simulate user input
    inputs = iter(["A", "Y", "B", "Y", "C", "N"])
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    
    game = Game()
    game.set_up_players()
    
    assert len(game.players) == 3