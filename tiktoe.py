# Tic-Tac-Toe Game in Python

# Initialize the board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (a tie)
def check_tie(board):
    return all([cell != " " for row in board for cell in row])

# Main game loop
current_player = "X"
while True:
    print_board(board)
    print(f"Player {current_player}'s turn.")
    
    # Get the player's move
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 2.")

    # Make the move
    board[row][col] = current_player

    # Check for a win or a tie
    if check_win(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        break

    # Switch to the other player
    current_player = "O" if current_player == "X" else "X"
