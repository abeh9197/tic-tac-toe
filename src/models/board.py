from typing import List


class Board:
    def __init__(self) -> None:
        pass

    def initialize(self) -> List:
        return [[0 for _ in range(3)] for n in range(3)]
