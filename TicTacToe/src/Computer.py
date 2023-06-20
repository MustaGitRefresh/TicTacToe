from Tracker import Tracker
import random


class Computer:
    def __init__(self):
        self.move = "X"  # Set the move for the computer as 'X'
        self.tracker = Tracker()  # created a instance of Tracker class

    def computer_play(self, buttons, game_board):
        if self.tracker.whose_turn == "C":
            game_board_copy = game_board.copy()  # Make a copy of the game board

            # Create a list of available moves by filtering out non-empty squares
            available_moves = [key for key, val in game_board_copy.items() if val == ""]

            if available_moves:
                # Randomly select a move from the available moves
                selected_move = random.choice(available_moves)
                print(selected_move)

                # Update the game board with the computer's move
                game_board_copy[selected_move] = self.move

                # Update the GUI button text with the computer's move
                buttons[selected_move].config(text=self.move, state='disabled')

                # Update the game board and user's move list
                game_board = game_board_copy
