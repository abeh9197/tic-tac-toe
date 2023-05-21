"""
board.py
"""
from typing import List
from .cell import Cell



class Board:
    """
    Get cells in initialize method.
    """
    def __init__(self) -> None:
        pass

    def initialize(self) -> List:
        """
        Initialize board.
        """
        return [[Cell.from_number(0) for _ in range(3)] for n in range(3)]
