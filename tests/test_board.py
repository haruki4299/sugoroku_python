import pytest
from src.board import Board

def test_board_length():
    board = Board(100)
    assert board.goal == 100