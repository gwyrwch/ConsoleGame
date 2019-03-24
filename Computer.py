from Player import Player
import random


class Computer(Player):
    def __init__(self, field):
        super().__init__(field)

    def make_a_move(self):
        if not len(self.field.possible_moves):
            return False

        move_num = random.randrange(0, len(self.field.possible_moves))
        move = self.field.possible_moves[move_num]
        self.field.update_field(
            move[0],
            move[1],
            move[2]
        )

        return True
