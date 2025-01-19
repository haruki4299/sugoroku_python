from src.square import Square

class Board:
    def __init__(self):
        self.goal = 100
        
        # Map the square location to each square. 
        # If the square has no effect it will not be in the map.
        self.squares = {}
        
    def add_special_square(self, location: int, square: Square) -> None:
        # The first and last square should not be a special one.
        if 1 < location < self.goal:
            self.squares[location] = square