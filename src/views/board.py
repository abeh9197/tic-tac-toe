from models.board import Board


def print_current(board: Board) -> None:
    """
    Print current board on terminal.
    """
    print("+---+---+---+")
    for i, row in enumerate(board):
        print("|", row[0], "|", row[1], "|", row[2], "|")
        if i != 2:
            print("+---+---+---+")
    print("+---+---+---+")