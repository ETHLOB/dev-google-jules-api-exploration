import unittest
from unittest.mock import patch
from tictactoe import (
    create_board,
    make_move,
    check_win,
    check_draw,
    get_player_input
)

class TestTicTacToe(unittest.TestCase):

    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertEqual(len(row), 3)
            self.assertTrue(all(cell == " " for cell in row))

    def test_make_move(self):
        board = create_board()
        make_move(board, 1, 1, "X")
        self.assertEqual(board[1][1], "X")
        make_move(board, 0, 2, "O")
        self.assertEqual(board[0][2], "O")

    def test_check_win(self):
        # Horizontal wins
        board_x_h = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        self.assertTrue(check_win(board_x_h, "X"))
        board_o_h = [[" ", " ", " "], ["O", "O", "O"], [" ", " ", " "]]
        self.assertTrue(check_win(board_o_h, "O"))

        # Vertical wins
        board_x_v = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
        self.assertTrue(check_win(board_x_v, "X"))
        board_o_v = [[" ", "O", " "], [" ", "O", " "], [" ", "O", " "]]
        self.assertTrue(check_win(board_o_v, "O"))

        # Diagonal wins
        board_x_d1 = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
        self.assertTrue(check_win(board_x_d1, "X"))
        board_o_d1 = [["O", " ", " "], [" ", "O", " "], [" ", " ", "O"]]
        self.assertTrue(check_win(board_o_d1, "O"))
        board_x_d2 = [[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]]
        self.assertTrue(check_win(board_x_d2, "X"))
        board_o_d2 = [[" ", " ", "O"], [" ", "O", " "], ["O", " ", " "]]
        self.assertTrue(check_win(board_o_d2, "O"))

        # No win
        board_no_win = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", " "]]
        self.assertFalse(check_win(board_no_win, "X"))
        self.assertFalse(check_win(board_no_win, "O"))
        board_empty = create_board()
        self.assertFalse(check_win(board_empty, "X"))

    def test_check_draw(self):
        board_draw = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
        self.assertTrue(check_draw(board_draw))

        board_not_draw_empty = create_board()
        self.assertFalse(check_draw(board_not_draw_empty))

        board_not_draw_winner = [["X", "X", "X"], [" ", "O", " "], ["O", " ", " "]]
        self.assertFalse(check_draw(board_not_draw_winner)) # Not a draw if someone can win
        
        board_not_draw_in_progress = [["X", "O", "X"], ["X", " ", "O"], ["O", "X", " "]]
        self.assertFalse(check_draw(board_not_draw_in_progress))

    @patch('builtins.input', side_effect=['1', '1'])
    def test_get_player_input_valid(self, mock_input):
        board = create_board()
        player_symbol = "X"
        row, col = get_player_input(player_symbol, board)
        self.assertEqual((row, col), (1, 1))

    @patch('builtins.input', side_effect=['0', '0', '1', '1']) # First try occupied, then valid
    @patch('builtins.print') # Suppress print output during test
    def test_get_player_input_invalid_occupied(self, mock_print, mock_input):
        board = create_board()
        make_move(board, 0, 0, "O") # Occupy cell (0,0)
        player_symbol = "X"
        row, col = get_player_input(player_symbol, board)
        self.assertEqual((row, col), (1, 1))
        mock_print.assert_any_call("Cell already taken. Choose an empty cell.")

    @patch('builtins.input', side_effect=['5', '5', '0', '1']) # First try out of bounds, then valid
    @patch('builtins.print') # Suppress print output during test
    def test_get_player_input_invalid_out_of_bounds(self, mock_print, mock_input):
        board = create_board()
        player_symbol = "X"
        row, col = get_player_input(player_symbol, board)
        self.assertEqual((row, col), (0, 1))
        mock_print.assert_any_call("Invalid input. Row and column must be between 0 and 2.")

    @patch('builtins.input', side_effect=['a', 'b', '0', '2']) # First try non-integer, then valid
    @patch('builtins.print') # Suppress print output during test
    def test_get_player_input_invalid_non_numeric(self, mock_print, mock_input):
        board = create_board()
        player_symbol = "X"
        row, col = get_player_input(player_symbol, board)
        self.assertEqual((row, col), (0, 2))
        mock_print.assert_any_call("Invalid input. Please enter numbers.")

if __name__ == '__main__':
    unittest.main()
