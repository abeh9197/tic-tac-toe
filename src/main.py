"""
三目並べ tic-tac-toe
"""
from views import print_current, acquire_input
from models import Board, Game, players_input


def main():
    """
    Need loop.
    """
    board = Board()
    game = Game()
    current_board = board.initialize()
    print_current(board=current_board)
    for col_or_row in game.input_:
        acquire_input(col_or_row=col_or_row)
        input_ = players_input()
        print(input_)


if __name__ == "__main__":
    main()