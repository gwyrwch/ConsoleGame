size = 8


class GameField:
    def __init__(self):
        self.current_field = [[''] * 8 for i in range(8)]
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
        if color == 0:
            self.current_field[i_coord][j_coord] = 'b'
        elif color == 1:
            self.current_field[i_coord][j_coord] = 'r'
        elif color == 2:
            self.current_field[i_coord][j_coord] = 'g'

    @staticmethod
    def delete_from_possible(possible_moves, i_coord, j_coord, color):
        if not len(possible_moves):
            print('Cannot move anywhere')
            exit(335)

        for i in range(i_coord - 1, i_coord + 2):
            for j in range(j_coord - 1, j_coord + 2):
                if 0 < i < size and 0 < j < size and [i, j, color] in possible_moves:
                    possible_moves.remove([i, j, color])

