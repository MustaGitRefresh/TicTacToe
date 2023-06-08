import random


def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")


def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False


def computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_winner(board, "O"):
                    return True
                else:
                    board[i][j] = " "

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board, "X"):
                    board[i][j] = "O"
                    return False
                else:
                    board[i][j] = " "

    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if make_move(board, row, col, "O"):
            break

    return False


def player_move(board):
    while True:
        move = input("Enter your move (row column): ")
        move = move.strip().split()
        if len(move) != 2:
            print("Invalid input. Please enter two numbers.")
            continue
        row, col = move
        if not row.isdigit() or not col.isdigit():
            print("Invalid input. Please enter valid numbers.")
            continue
        row, col = int(row), int(col)
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid input. Please enter numbers within the range.")
            continue
        if make_move(board, row, col, "X"):
            break
        else:
            print("Invalid move. That cell is already occupied.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. The computer is 'O'.")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You won!")
            break

        if computer_move(board):
            print("Computer wins!")
            break

    print("Game Over.")


play_game()
