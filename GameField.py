from termcolor import colored
size = 8


class GameField:
    def __init__(self):
        self.current_field = [['O'] * 8 for i in range(8)]
        self.possible_moves = self.init_possible_moves()

    @staticmethod
    def init_possible_moves():
        moves = []
        for i in range(8):
            for j in range(8):
                for k in range(3):
                    moves.append([i, j, k])
        return moves

    def update_field(self, i_coord, j_coord, color):
        self.delete_from_possible(self.possible_moves, i_coord, j_coord, color)

        map_ind_to_color = dict([
            (0, 'B'),
            (1, 'R'),
            (2, 'G')
        ])
        self.current_field[i_coord][j_coord] = map_ind_to_color[color]

    @staticmethod
    def delete_from_possible(possible_moves, i_coord, j_coord, color):
        for i in range(i_coord - 1, i_coord + 2):
            for j in range(j_coord - 1, j_coord + 2):
                if 0 <= i < size and 0 <= j < size and [i, j, color] in possible_moves:
                    possible_moves.remove([i, j, color])

    def print_current_field(self):
        for i in range(size + 1):
            print(colored(i if i != 0 else '  ', 'grey', 'on_cyan', attrs=['underline']), end='')
        print()

        map_color = dict([
            ('B', 'blue'),
            ('R', 'red'),
            ('G', 'green'),
            ('O', 'grey')
        ])

        for i in range(size):
            for j in range(size + 1):
                if j == 0:
                    print(colored(str(i + 1) + '|', 'grey', 'on_cyan'), end='')
                else:
                    cur_cell = self.current_field[i][j - 1]
                    print(
                        colored(
                            cur_cell, map_color[cur_cell],
                            attrs=['bold']
                        ),
                        end=''
                    )
            print()
