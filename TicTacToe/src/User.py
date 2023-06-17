from Tracker import Tracker


class User:
    def __init__(self):
        self.tracker = Tracker()
        self.move = "O"  # Set the move for the user as 'O'
        self.user_move = []
        user_move_list = [self.tracker.game_board[i] for i in self.user_move]
        print(user_move_list)

    def append_user_move(self, key):
        self.user_move.append(key)
