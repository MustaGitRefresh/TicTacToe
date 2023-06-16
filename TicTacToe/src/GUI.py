from tkinter import Tk
import tkinter
from Tracker import Tracker


class Board:
    def __init__(self):
        self.tracker = Tracker()
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
        print(keys)
        self.tracker.game_board[keys[0]] = 'X'
        self.buttons[keys[0]].config(text=self.tracker.game_board[keys[0]])
        print(self.tracker.game_board)


window = Tk()
board = Board()


def run():
    window.mainloop()
