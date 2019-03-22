class Player:
    def __init__(self, field):
        self.field = field

    def make_a_move(self):
        if not len(self.field.possible_moves):
            return False

        while True:
            print('Please input coordinates and color')
            i, j, color = map(int, input().split(' '))

            if [i, j, color] in self.field.possible_moves:
                self.field.update_field(i, j, color)
                break
            else:
                print('Impossible move. Try again')
                continue
