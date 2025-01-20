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
        