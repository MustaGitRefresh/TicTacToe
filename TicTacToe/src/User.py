class User:
    def __init__(self):
        self.move = "O"  # Set the move for the user as 'O'
        self.user_move = []
        self.user_game_patterns = None

    def append_user_move(self, key, game_board):
        self.user_move.append(key)
        self.user_game_patterns = {i: game_board[i] for i in self.user_move}
        print(f"User game patterns {self.user_game_patterns}")

