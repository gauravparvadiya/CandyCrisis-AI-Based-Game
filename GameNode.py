# Using python3


class GameNode:

    def __init__(self, node_name, node_candy_setup, node_heuristic, node_parent, previous_move):
        self.node_name = node_name
        self.node_candy_setup = node_candy_setup
        self.node_heuristic = node_heuristic
        self.node_parent = node_parent
        self.previous_move = previous_move

    def get_node_candy_setup(self):
        return self.node_candy_setup

    def get_node_parent(self):
        return self.node_parent

    def get_node_name(self):
        return self.node_name

