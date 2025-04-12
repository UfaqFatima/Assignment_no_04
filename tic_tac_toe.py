import numpy as np

# Tic-Tac-Toe board
board = np.array([[" " for _ in range(3)] for _ in range(3)])

# Function to print the board
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner():
    for i in range(3):
        # Rows and Columns Check
        if all(board[i, :] == board[i, 0]) and board[i, 0] != " ":
            return board[i, 0]
        if all(board[:, i] == board[0, i]) and board[0, i] != " ":
            return board[0, i]
    
    # Diagonal Check
    if all(board.diagonal() == board[0, 0]) and board[0, 0] != " ":
        return board[0, 0]
    if all(np.fliplr(board).diagonal() == board[0, 2]) and board[0, 2] != " ":
        return board[0, 2]
    
    return None  # No winner yet

# Main game loop
def play_game():
    player = "X"
    for turn in range(9):
        print_board()
        print(f"\nPlayer {player}, enter your move (row and column: 0 1 or 2 2): ")
        
        while True:
            try:
                row, col = map(int, input().split())
                if board[row, col] == " ":
                    board[row, col] = player
                    break
                else:
                    print("⚠️ Invalid move! Cell already occupied. Try again:")
            except (ValueError, IndexError):
                print("⚠️ Invalid input! Enter row and column as two numbers (0-2). Try again:")

        # Check for winner
        winner = check_winner()
        if winner:
            print_board()
            print(f"\n🎉 Player {winner} wins! 🎉")
            return
        
        # Switch player
        player = "O" if player == "X" else "X"
    
    print_board()
    print("\nIt's a Draw! 🤝")

# Run the game
play_game()
# Footer
import streamlit as st
st.markdown(
    "<div style='text-align: center; padding: 10px; color: #FF0000;'>Made with love by Ufaq Fatima🚀</div>",
    unsafe_allow_html=True
)
# This code is a simple console-based Tic-Tac-Toe game. It uses NumPy for the board representation and includes functions to print the board, check for a winner, and handle player moves. The game alternates between two players (X and O) until a winner is found or the game ends in a draw.
# The game is played in the console, and players input their moves by specifying the row and column indices.