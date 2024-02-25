def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_move(board, player_symbol):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "":
                board[row][col] = player_symbol
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board, player_symbol):
    # Check rows
    for row in board:
        if all(square == player_symbol for square in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player_symbol for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player_symbol for i in range(3)) or all(board[i][2 - i] == player_symbol for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(all(square != "" for square in row) for row in board)

def main():
    board = [["" for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        player_move(board, players[current_player])

        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
