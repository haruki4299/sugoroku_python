import pytest
from src.board import Board

def test_board_creation():
    board = Board()
    assert board.goal == 100