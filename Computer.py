from Player import Player
import random


class Computer(Player):
    def __init__(self, field):
        super().__init__(field)

    def make_a_move(self):
        if not len(self.field.possible_moves):
            return False

        move = random.randrange(0, len(self.field.possible_moves))
        self.field.update_field(
            self.field.possible_moves[move][0],
            self.field.possible_moves[move][1],
            self.field.possible_moves[move][2]
        )

        return True
