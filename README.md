# Tic-Tac-Toe Game

A classic command-line Tic-Tac-Toe game implemented in Python. Two players take turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If all nine squares are filled and no player has three in a row, the game is a draw.

## Project Structure

- `tictactoe.py`: Contains the main game logic.
- `test_tictactoe.py`: Contains unit tests for the game.
- `pyproject.toml`: Project configuration file for `uv` (though not strictly needed for this simple project, it's included for good practice).
- `README.md`: This file, providing information about the project.

## How to Run the Game

You will need Python 3 installed on your system. This game has no external dependencies.

### 1. Using a Virtual Environment with `uv` (Recommended for consistency)

This project includes a `pyproject.toml` file and can be managed with `uv`, a fast Python package installer and project manager.

a. **Set up a virtual environment using `uv`:**
   Open your terminal in the project root directory and run:
   ```bash
   uv venv
   ```
   This will create a virtual environment named `.venv` in the project directory.

b. **Activate the virtual environment:**
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   You should see `(.venv)` at the beginning of your terminal prompt.

c. **Run the game:**
   Once the environment is activated, you can run the game using:
   ```bash
   python tictactoe.py
   ```

### 2. Running Directly (without a virtual environment)

Since this game has no external dependencies, you can also run it directly if you have Python 3 installed:

```bash
python tictactoe.py
```

The game will then start in your console. Follow the on-screen prompts to play. Player X goes first. Enter your moves by specifying the row (0-2) and column (0-2).

## How to Run Tests

The unit tests are written using Python's built-in `unittest` module.

### 1. Using `uv` (Recommended if the virtual environment is active)

If you have activated the `uv` virtual environment as described above, you can run the tests using `uv`:

To discover and run all tests:
```bash
uv run python -m unittest discover
```
Alternatively, to run the specific test file:
```bash
uv run python -m unittest test_tictactoe.py
```

### 2. Running Directly with Python

You can also run the tests directly using your Python interpreter:

To discover and run all tests (useful if you have multiple test files or a specific test structure):
```bash
python -m unittest discover
```
Or to run the specific test file:
```bash
python -m unittest test_tictactoe.py
```

All tests should pass, indicating the game logic is working as expected.
