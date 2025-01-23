from pathlib import Path

from src.square import Square
from src.board import Board
from src.player import Player
import src.utils as utils

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_player = 0
        
    def add_player(self, player: Player) -> None:
        self.players.append(player)
        
    def set_up_players(self) -> None:
        while True:
            new_player_name = utils.ask_for_player_name()
            new_player = Player(new_player_name)
            self.add_player(new_player)
            if not utils.will_add_another_player():
                break
            
    def set_up_board_squares(self) -> None:
        PROJECT_ROOT = Path(__file__).resolve().parent.parent
        INPUT_FILES_DIR = PROJECT_ROOT / "input_files"
        input_file_path = INPUT_FILES_DIR / "board1.txt"
        
        squares_info = utils.read_square_input_file(input_file_path)
        
        self.load_board_squares(squares_info)
        
    def load_board_squares(self, square_information: list[str]) -> None:
        for square in square_information:
            square_information_array = list(map(int, square.split()))
            self.read_and_load_square_information(square_information_array)
            
    def read_and_load_square_information(self, square_array: list[int]) -> bool:
        square_location = square_array[0]
        extra_movement = square_array[1]
        rest_inflicted = square_array[2]
        warp_location = square_array[3]
        
        new_square = Square()
        new_square.set_amount_extra_move_by_square(extra_movement)
        new_square.set_amount_rest_inflicted_by_square(rest_inflicted)
        new_square.set_warp_location(warp_location)
        
        return self.board.add_special_square(square_location, new_square)
        
    # def get_player(self) -> Player:
    #     return self.players[self.current_player]
    
    # def set_to_next_player_turn(self) -> None:
    #     self.current_player = self.current_player + 1 % len(self.players)
    
    # def get_current_player_location(self) -> int:
    #     current_player = self.get_player()
    #     current_location = current_player.get_current_location()
    #     return current_location
    
    # def check_game_end(self) -> bool:
    #     return self.board.goal == self.get_current_player_location()
    
    # def player_turn(self) -> None:
    #     current_player = self.get_player()
    #     dice_roll_outcome = current_player.roll_die()
        