class User:
    def __init__(self):
        self.move = "O"  # Set the move for the user as 'O'
        self.user_move = []  # Initialize an empty list to store user's moves
        self.user_game_patterns = None  # Initialize user's game patterns as None

    def append_user_move(self, key, game_board):
        self.user_move.append(key)  # Append the key (move) to the user's move list
        self.user_game_patterns = {i: game_board[i] for i in self.user_move}  # Update user's game patterns based on
        # current moves
        print(f"User game patterns {self.user_game_patterns}")  # Print user's game patterns for debugging or display
        # purposes

    def check_validate_move(self):
        if self.user_move in self.user_move:
            return False
