from views import print_current
from models import Board

def main():
    board = Board()
    current_board = board.initialize()
    print_current(board=current_board)


if __name__ == "__main__":
    main()