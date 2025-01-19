class Square:
    def __init__(self) -> None:
        self.extra_move = 0
        self.inflict_rest = 0
        self.warp_location = -1
        
    def set_amount_extra_move_by_square(self, number: int) -> None:
        self.extra_move = number
        
    def get_amount_extra_move_by_square(self) -> int:
        return self.extra_move
        
    def set_amount_rest_inflicted_by_square(self, number: int) -> None:
        # The amount of extra rests should be positive
        if number > 0:
            self.inflict_rest = number
    
    def get_amount_rest_inflicted_by_square(self) -> int:
        return self.inflict_rest
            
    def set_warp_location(self, new_location: int) -> None:
        self.warp_location = new_location
        
    def get_warp_location(self) -> int:
        return self.warp_location