import unittest
from src.models.cell import CellValue, Cell


class TestBoard(unittest.TestCase):
    """
    Test class of board.py
    """
    def test_from_number(self):
        """
        Test method for initialize (Equal)
        """
        expected = CellValue.BLANK
        actual = Cell.from_number(0).value
        self.assertEqual(expected, actual)
