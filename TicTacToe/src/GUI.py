from tkinter import Tk
import tkinter
from tkinter import DISABLED
from Tracker import Tracker
from User import User
from Computer import Computer


class Board:
    def __init__(self):
        self.move_value = " "  # Represents the current move value ("X" or "O")
        self.tracker = Tracker()  # Object for tracking game progress
        self.user = User()  # Object representing the user
        self.computer = Computer()  # Object representing the computer
        self.root = window  # Root window of the GUI
        self.button_frame = tkinter.Frame(self.root)  # Frame to hold the buttons
        self.button_frame.pack(anchor=tkinter.CENTER, pady=50)  # Pack the frame in the center with some padding
        self.buttons = self.create_board_buttons()  # Create the game board buttons
        self.center_window()  # Center the window on the screen

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()  # Get the screen width
        screen_height = self.root.winfo_screenheight()  # Get the screen height
        window_height = 400
        window_width = 500
        x = (screen_width - window_width) // 2  # Calculate the x-coordinate for centering the window
        y = (screen_height - window_height) // 2  # Calculate the y-coordinate for centering the window
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Set the window's geometry

    def create_board_buttons(self):
        buttons = dict()
        for i in range(9):
            button = tkinter.Button(self.button_frame, width=10, height=5)  # Create a button
            button.grid(row=i // 3, column=i % 3)  # Grid layout for the button
            button.config(command=lambda btn=button: self.button_after_click_command(btn))  # Configure button command
            buttons.update({i + 1: button})  # Add button to the dictionary
        return buttons

    def button_after_click_command(self, button):
        keys = [key for key, val in self.buttons.items() if
                val == button]  # Find the key corresponding to the clicked button
        key = keys[0]
        self.checkWhoseMove()  # Determine whose turn it is
        self.tracker.game_board[key] = self.move_value  # Update the game board with the move
        self.buttons[key].config(text=self.tracker.game_board[key])  # Update the button text
        self.buttons[key].config(state=DISABLED)
        print(self.tracker.game_board)
        if self.move_value == self.user.move:
            self.user.append_user_move(key, self.tracker.game_board)  # Append user's move to the list of moves
        self.checkWhoseMove()  # Update move_value based on the current turn
        if self.tracker.whose_turn == "C":
            self.tracker.game_board = self.computer.computer_play(self.buttons, self.tracker.game_board,
                                                                  self.tracker.whose_turn)  # Computer's move

    def checkWhoseMove(self):
        if self.tracker.whose_turn == "C":
            self.move_value = self.computer.move  # Set the move value to the computer's move
            print(f"whose move {self.tracker.game_board}")
            self.tracker.whose_turn = 'U'  # Update the tracker to indicate user's turn
        elif self.tracker.whose_turn == "U":
            self.move_value = self.user.move  # Set the move value to the user's move
            self.computer.computer_play(self.buttons, self.tracker.game_board,
                                        self.tracker.whose_turn)
            self.tracker.whose_turn = "C"  # Update the tracker to indicate computer's turn


window = Tk()
board = Board()


def run():
    window.mainloop()  # Start the main event loop for the GUI
