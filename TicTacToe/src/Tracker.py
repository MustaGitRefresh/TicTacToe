# This class will represent the state of the game board
class Tracker:
    """
    This class will represent the whole game board
    and keep track of the moves
    """

    def __init__(self):
        self._whose_turn = "C"  # Variable to track whose turn it is ('C' for computer)
        self.game_board = {  # Dictionary to represent the game board with empty squares
            key: "" for key in range(1, 10)
        }

        # Define patterns for winning the game
        lst = [i for i in range(1, 10)]
        self.game_patterns = {
            'left_diagonal': [i for i in range(1, len(self.game_board.keys()) + 1, 4)],  # Left diagonal pattern
            'right_diagonal': [i for i in range(3, len(self.game_board.keys()), 2)],  # Right diagonal pattern
            'columns_cross': [lst[i:i + 3] for i in range(0, len(lst), 3)],  # Columns pattern
            'rows_cross': []  # Rows pattern (to be calculated later)
        }

        # Calculate rows pattern by transposing the columns pattern
        self.sub_lists = self.game_patterns['columns_cross']
        zip_sub_list = list(zip(*self.sub_lists))
        for i in zip_sub_list:
            self.game_patterns['rows_cross'].append(list(i))

    @property
    def whose_turn(self):
        return self._whose_turn

    @whose_turn.setter
    def whose_turn(self, now_turn):
        self._whose_turn = now_turn


if __name__ == '__main__':
    tracker = Tracker()
    print(tracker.game_board)  # Print the initial game board state
    print(tracker.game_patterns)  # Print the predefined game patterns
