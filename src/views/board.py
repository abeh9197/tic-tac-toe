from models.board import Board


def print_current(board: Board) -> None:
    """
    Print current board on terminal.
    """
    print("      1   2   3  ")
    print("    +---+---+---+")
    for i, row in enumerate(board):
        print(i + 1, "  |", row[0], "|", row[1], "|", row[2], "|")
        if i != 2:
            print("    +---+---+---+")
    print("    +---+---+---+")
