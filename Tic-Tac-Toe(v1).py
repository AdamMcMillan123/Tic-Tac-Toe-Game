import tkinter as tk
from tkinter import messagebox

# Constants for configuration
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 500
BUTTON_WIDTH, BUTTON_HEIGHT = 6, 3
BUTTON_BG = '#00ff00'  # Bright neon green for buttons
BUTTON_FG = 'black'     # Button text color
RESET_BG = '#00ff00'    # Bright neon green for reset button
FONT = ('Courier', 20, 'bold')  # Font for buttons
BUTTON_BORDER_WIDTH = 2  # Border width for buttons
GRADIENT_COLOR_START = (0, 100, 0)  # Dark green
GRADIENT_COLOR_END = (0, 0, 0)  # Black

# Function to create a gradient background
def create_gradient(canvas, color1, color2, height):
    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * (i / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (i / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (i / height))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, WINDOW_WIDTH, i, fill=color)

# Function to create buttons with common configurations
def create_button(master, text, row, col, command):
    button = tk.Button(
        master, text=text, width=BUTTON_WIDTH, height=BUTTON_HEIGHT,
        font=FONT, bg=BUTTON_BG, fg=BUTTON_FG, activebackground='yellow',
        bd=BUTTON_BORDER_WIDTH, highlightbackground='black', highlightcolor='black',
        command=command
    )
    button.place(x=col * 100 + 50, y=row * 100 + 50)
    return button

# Function to check for a winner or draw
def check_winner():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '':
            return board[combo[0]]  # Return the winning player ('X' or 'O')

    return 'Draw' if '' not in board else None

# Function to handle button click events
def on_button_click(index):
    global player
    if board[index] == '':
        board[index] = player
        buttons[index].config(text=player, state="disabled")

        result = check_winner()
        if result:
            messagebox.showinfo("Tic-Tac-Toe", f"{result} wins!" if result != 'Draw' else "It's a draw!")
            reset_game()
        else:
            player = 'O' if player == 'X' else 'X'  # Switch player

# Function to reset the game
def reset_game():
    global player
    player = 'X'  # X always starts the game
    for i in range(9):
        board[i] = ''
        buttons[i].config(text='', state="normal")

# Initialize the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe Arcade")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")  # Window size
root.resizable(False, False)  # Prevent resizing
root.configure(bg='black')  # Set a solid black background for the window

# Create a canvas for the gradient background
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack(fill=tk.BOTH, expand=True)

# Create the gradient
create_gradient(canvas, GRADIENT_COLOR_START, GRADIENT_COLOR_END, WINDOW_HEIGHT)

# Variables to track the game state
player = 'X'  # Player X starts the game
board = ['' for _ in range(9)]  # Empty 3x3 board
buttons = []  # List to store buttons for easy access

# Create the 3x3 grid of buttons
for i in range(3):
    for j in range(3):
        buttons.append(create_button(root, '', i, j, lambda index=i*3+j: on_button_click(index)))

# Add a reset button below the grid
reset_button = tk.Button(root, text='RESET GAME', width=10, height=2, font=FONT,
                         bg=RESET_BG, fg=BUTTON_FG, activebackground='yellow',
                         bd=BUTTON_BORDER_WIDTH, highlightbackground='black', highlightcolor='black',
                         command=reset_game)
reset_button.place(x=120, y=400)  # Positioned below the grid

# Start the tkinter main event loop
root.mainloop()
