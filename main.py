from GameField import GameField
from Computer import Computer
from Player import Player

if __name__ == '__main__':
    field = GameField()
    computer = Computer(field)
    player = Player(field)
    playing = True

    while playing:
        playing = computer.make_a_move()
        if not playing:
            print('Computer lose.')

        player.make_a_move()

        for i in field.current_field:
            print(i)

    print('Player lose')

