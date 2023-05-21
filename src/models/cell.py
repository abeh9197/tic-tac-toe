"""
Cell and CellValue.
"""
from __future__ import annotations
from enum import Enum


class CellValue(Enum):
    """
    Values of each cell.
    """
    BLANK = {"id_":0, "type_": "blank", "view": " "}
    NOUGHT = {"id_":1, "type_": "nought", "view": "O"}
    CROSS =  {"id_":2, "type_": "cross", "view": "X"}

    @staticmethod
    def from_number(num: int) -> CellValue:
        """
        Return Cell type from argument number.
        """
        for cell in CellValue:
            if cell.value["id_"] == num:
                return cell
        raise ValueError("Invalid number")

class Cell:
    """
    Constructed from staticmethod: 'from_number'.
    """
    def __init__(self, value: CellValue) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value.value["view"])

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return int(self.value["id_"])

    def __eq__(self, other: Cell) -> bool:
        return self.value == other.value

    @staticmethod
    def from_number(num: int) -> Cell:
        """
        Return constructed cell from number
        """
        return Cell(CellValue.from_number(num))


