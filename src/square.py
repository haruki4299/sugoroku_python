class Square:
    def __init__(self) -> None:
        self.extra_move = 0
        self.inflict_rest = 0
        self.warp_location = -1
        
    def set_amount_extra_move_by_square(self, number: int) -> None:
        self.extra_move = number
        
    def set_amount_rest_inflicted_by_square(self, number: int) -> None:
        # The amount of extra rests should be positive
        if number > 0:
            self.inflict_rest = number
            
    def set_warp_location(self, new_location: int) -> None:
        self.warp_location = new_location