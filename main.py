from GameField import GameField
from Computer import Computer
from Player import Player
from termcolor import colored


if __name__ == '__main__':
    field = GameField()
    computer = Computer(field)
    player = Player(field)
    playing = True

    while playing:
        playing = computer.make_a_move()
        if not playing:
            print(colored('You won! Computer lose', 'yellow'))
            break

        field.print_current_field()

        playing = player.make_a_move()
        if not playing:
            print(colored('You lose', 'red'))
            break



