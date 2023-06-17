from tkinter import Tk
import tkinter
from Tracker import Tracker
from User import User
from Computer import Computer


class Board:
    def __init__(self):
        self.move_value = " "
        self.tracker = Tracker()
        self.user = User()
        self.computer = Computer()
        self.root = window
        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(anchor=tkinter.CENTER, pady=50)
        self.buttons = self.create_board_buttons()
        self.center_window()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_height = 400
        window_width = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_board_buttons(self):
        buttons = dict()
        for i in range(9):
            button = tkinter.Button(self.button_frame, width=10, height=5)
            button.grid(row=i // 3, column=i % 3)
            button.config(command=lambda btn=button: self.button_after_click_command(btn))
            buttons.update({i + 1: button})
        return buttons

    def button_after_click_command(self, button):
        keys = [key for key, val in self.buttons.items() if val == button]
        key = keys[0]
        self.checkWhoseMove(key)
        self.tracker.game_board[key] = self.move_value
        self.buttons[key].config(text=self.tracker.game_board[key])
        print(self.tracker.game_board)

    def checkWhoseMove(self, move_position):
        if self.tracker.whose_turn == "C":
            self.move_value = Computer().move
            self.tracker.whose_turn = 'U'
        elif self.tracker.whose_turn == "U":
            self.move_value = User().move
            self.tracker.whose_turn = "C"
            self.user.append_user_move(move_position)


window = Tk()
board = Board()


def run():
    window.mainloop()
