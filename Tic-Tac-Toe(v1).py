import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables to track the game state
player = 'X'  # Player X starts the game
board = ['' for _ in range(9)]  # Empty 3x3 board
buttons = []  # List to store buttons for easy access

# Function to check for a winner or draw
def check_winner():
    # All possible winning combinations (rows, columns, diagonals)
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]

    # Check for a winner
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '':
            return board[combo[0]]  # Return the winning player ('X' or 'O')

    # Check for a draw (all cells are filled but no winner)
    if '' not in board:
        return 'Draw'

    # No winner or draw yet
    return None

# Function to handle button click events
def on_button_click(index):
    global player

    # If the clicked cell is empty
    if board[index] == '':
        # Update the board and button text
        board[index] = player
        buttons[index].config(text=player, state="disabled")

        # Check for a winner or draw
        result = check_winner()
        if result:
            if result == 'Draw':
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {result} wins!")
            reset_game()  # Reset the game after a win/draw
        else:
            # Switch player after a successful move
            player = 'O' if player == 'X' else 'X'

# Function to reset the game
def reset_game():
    global player, board
    player = 'X'  # X always starts the game
    board = ['' for _ in range(9)]  # Clear the board
    for button in buttons:
        button.config(text='', state="normal")  # Reset the buttons

# Create the 3x3 grid of buttons
for i in range(9):
    button = tk.Button(root, text='', width=10, height=3, font=('Arial', 24),
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)  # Place button in a 3x3 grid
    buttons.append(button)

# Add a reset button below the grid
reset_button = tk.Button(root, text='Reset Game', width=10, height=2, font=('Arial', 14), command=reset_game)
reset_button.grid(row=3, column=1)

# Start the tkinter main event loop
root.mainloop()
