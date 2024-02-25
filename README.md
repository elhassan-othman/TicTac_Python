# TicTac_Python

## Tic Tac Toe Game in Python

This project involves building a Tic Tac Toe game in Python without a graphical user interface (GUI). The game is played on the command line, where users enter their moves as text inputs. The project focuses on implementing game logic using Python's built-in data structures and control flow statements.

## Game Rules

- The game is played on a 3x3 grid.
- Players take turns placing their symbols (X or O) on the grid.
- The goal is to get three in a row horizontally, vertically, or diagonally.
- The game ends when one player gets three in a row or when the grid is full without any player achieving three in a row, resulting in a tie.

## Project Structure

1. **Design the Game Board:**
   - The game board is represented as a 3x3 list of lists.
   - Each element in the list represents a square on the board and is initially set to an empty string.

2. **Print the Game Board:**
   - The `print_board` function takes the game board as a parameter.
   - It uses loops to iterate through the rows and columns of the board, printing each square in the appropriate location.

3. **Handle Player Moves:**
   - The `player_move` function takes the game board and the current player's symbol as parameters.
   - It prompts the player for their move using `input()` and updates the game board with the player's symbol in the appropriate location.

4. **Check for a Win:**
   - The `check_win` function takes the game board and the current player's symbol as parameters.
   - It checks if any rows, columns, or diagonals of the board contain three of the player's symbols in a row.

5. **Check for a Tie:**
   - The `check_tie` function takes the game board as a parameter.
   - It checks if every square on the board has been filled, indicating a tie.

6. **Main Game Loop:**
   - The main game loop alternates between the two players.
   - In each iteration, it prints the current state of the game board, prompts the current player for their move, updates the game board, and checks if the game has been won or tied.
   - If the game has been won or tied, the loop ends, and the appropriate message is printed.

7. **Testing and Debugging:**
   - The project includes testing the game by playing it and ensuring that it correctly handles player moves, checks for wins and ties, and prints appropriate messages.
   - Debug any issues that arise during testing.