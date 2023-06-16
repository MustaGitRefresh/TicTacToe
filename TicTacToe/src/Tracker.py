# This class will represent The state of game board

class Tracker:
    """
    This class will represent the whole game_board
    and keep track of the moves
    """
    def __init__(self):
        self.game_board = {
            key: "" for key in range(1, 10)
        }
        lst = [i for i in range(1, 10)]
        self.game_patterns = {
            'left_diagonal': [i for i in range(1, len(self.game_board.keys())+1, 4)],
            'right_diagonal': [i for i in range(3, len(self.game_board.keys()), 2)],
            'columns_cross': [lst[i:i+3] for i in range(0, len(lst), 3)],
            'rows_cross': []
        }
        self.sub_lists = self.game_patterns['columns_cross']
        zip_sub_list = list(zip(*self.sub_lists))
        for i in zip_sub_list:
            self.game_patterns['rows_cross'].append(list(i))


if __name__ == '__main__':
    tracker = Tracker()
    print(tracker.game_board)
    print(tracker.game_patterns)
