# Using python3


class GameBoard:
    candy_value = ""
    tile_name = ""
    possible_moves = []
    candy_object_left = None
    candy_object_right = None
    candy_object_up = None
    candy_object_down = None

    def __init__(self, candy_value, tile_name):
        self.candy_value = candy_value
        self.tile_name = tile_name

    def set_candy_value(self, candy_value):
        self.candy_value = candy_value

    def get_candy_value(self):
        return self.candy_value

    def get_tile_name(self):
        return self.tile_name

    def get_possible_moves(self):
        return self.possible_moves

    def set_possible_moves(self,possible_moves):
        self.possible_moves = possible_moves

    def set_candy_object_left(self,candy_object_left):
        self.candy_object_left = candy_object_left

    def set_candy_object_right(self, candy_object_right):
        self.candy_object_right = candy_object_right

    def set_candy_object_up(self, candy_object_up):
        self.candy_object_up = candy_object_up

    def set_candy_object_down(self, candy_object_down):
        self.candy_object_down = candy_object_down

    def get_candy_object_left(self):
        return self.candy_object_left

    def get_candy_object_right(self):
        return self.candy_object_right

    def get_candy_object_up(self):
        return self.candy_object_up

    def get_candy_object_down(self):
        return self.candy_object_down
