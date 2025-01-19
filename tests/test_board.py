import pytest
from src.board import Board
from src.square import Square

def test_board_creation():
    board = Board()
    assert board.goal == 100
    
def test_square_creation():
    square1 = Square()
    square1.set_amount_extra_move_by_square(1)
    
    square2 = Square()
    square2.set_amount_rest_inflicted_by_square(1)
    
    square3 = Square()
    square3.set_warp_location(10)
    
    assert square1.get_amount_extra_move_by_square() == 1
    assert square2.get_amount_rest_inflicted_by_square() == 1
    assert square3.get_warp_location() == 10
    
def test_square_addition_to_board():
    board = Board()
    
    square1 = Square()
    square1.set_amount_extra_move_by_square(1)
    
    board.add_special_square(10, square1)
    
    for i in range(1, 101):
        if i == 10:
            assert board.is_special_square(i)
            assert board.get_special_square(i).get_amount_extra_move_by_square() == 1
        else:
            assert not board.is_special_square(i)
    
    