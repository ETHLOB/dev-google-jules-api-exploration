def create_board():
    """Initializes and returns an empty 3x3 board."""
    return [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    """Prints the board to the console in a user-friendly format."""
    print("\n  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} " + "|".join(row))
        if i < 2:
            print("  -----")

def get_player_input(player_symbol, board):
    """
    Prompts the current player (player_symbol) to enter their move (row and column).
    Validates the input to ensure it's within bounds (0-2 for row and col) 
    and the chosen cell is empty.
    Returns the valid (row, col) tuple.
    """
    while True:
        try:
            row = int(input(f"Player {player_symbol}, enter row (0-2): "))
            col = int(input(f"Player {player_symbol}, enter column (0-2): "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input. Row and column must be between 0 and 2.")
            elif board[row][col] != " ":
                print("Cell already taken. Choose an empty cell.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except IndexError: # Should be caught by the first check, but good practice
            print("Invalid input. Row or column out of bounds.")


def make_move(board, row, col, player_symbol):
    """Updates the board with the player's move."""
    board[row][col] = player_symbol

def check_win(board, player_symbol):
    """
    Checks if the current player (player_symbol) has won.
    Returns True if a win condition is met (3 in a row, column, or diagonal), False otherwise.
    """
    # Check rows
    for row in board:
        if all(s == player_symbol for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player_symbol for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player_symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == player_symbol for i in range(3)):
        return True
    return False

def check_draw(board):
    """
    Checks if the game is a draw (all cells are filled and no one has won).
    Returns True if it's a draw, False otherwise.
    """
    for row in board:
        if any(s == " " for s in row):
            return False  # If any cell is empty, it's not a draw
    return True # All cells are filled

def play_game():
    """Main game loop for Tic-Tac-Toe."""
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        print(f"\nPlayer {current_player}'s turn.")
        
        row, col = get_player_input(current_player, board)
        make_move(board, row, col, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"\nCongratulations! Player {current_player} wins!")
            break
        
        if check_draw(board):
            display_board(board)
            print("\nIt's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
