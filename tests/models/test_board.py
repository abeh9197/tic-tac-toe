import unittest
from src.models.board import Board


class TestBoard(unittest.TestCase):
    """
    Test class of board.py
    """
    def test_initialize(self):
        """
        Test method for initialize (Equal)
        """
        board = Board()
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        actual = board.initialize()
        self.assertEqual(expected, actual)

    def test_initialize_not_equal(self):
        """
        Test method for initialize (Not Equal)
        """
        board = Board()
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        actual = board.initialize()
        self.assertNotEqual(expected, actual)
