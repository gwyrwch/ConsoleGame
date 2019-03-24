import random
from MathOperations import MathOperations

input_format = "{1-8} {1-8} {1-3}"


class Player:
    def __init__(self, field):
        self.field = field

    def make_a_move(self):
        if not len(self.field.possible_moves):
            return False

        while True:
            print('Please input coordinates and color in the following format: ', input_format)
            self.suggest_move(len(self.field.possible_moves), self.field.possible_moves)
            i, j, color = 0, 0, 0
            try:
                i, j, color = map(MathOperations.decrement, map(int, input().split(' ')))
            except ValueError:
                print('Invalid input. Try again.')
                continue

            if [i, j, color] in self.field.possible_moves:
                self.field.update_field(i, j, color)
                return True
            else:
                print('Impossible move. Try again')
                continue

    @staticmethod
    def suggest_move(in_range, possible_moves):
        move = random.randrange(in_range)
        print(' '.join(
            [
                'Move',
                str(list(map(MathOperations.increment, possible_moves[move]))),
                'is possible'
             ]
        ))
