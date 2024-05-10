import random

def create_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def get_player_input():
    player1 = input("Player 1, choose your marker: ")
    player2 = input("Player 2, choose your marker: ")
    return player1, player2

def place_marker(board, marker, position):
    row, col = position
    board[row][col] = marker

def win_check(board, marker):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == marker:
            return True
        if board[0][i] == board[1][i] == board[2][i] == marker:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == marker:
        return True
    if board[0][2] == board[1][1] == board[2][0] == marker:
        return True

    return False

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def full_board_check(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def player_choice(board):
    position = input("Enter your position (row, column): ")
    row, col = position.split(',')
    row = int(row)-1
    col = int(col)-1
    while row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
        position = input("Invalid position. Enter again: ")
        row, col = position.split(',')
        row = int(row)
        col = int(col)
    return row, col

def replay():
    replay = input("Do you want to play again? (y/n): ")
    return replay == 'y'

# Main game loop
while True:
    # Reset the board
    theBoard = create_board()

    # Get player input
    player1_marker, player2_marker = get_player_input()

    # Choose who goes first
    turn = choose_first()

    game_on = True
    while game_on:
        if turn == 'Player 1':
            # Player 1's turn

            # Print the board
            print_board(theBoard)

            # Get player 1's choice
            row, col = player_choice(theBoard)

            # Place player 1's marker on the board
            place_marker(theBoard, player1_marker, (row, col))

            # Check if player 1 has won
            if win_check(theBoard, player1_marker):
                print_board(theBoard)
                print("Player 1 wins!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    print_board(theBoard)
                    print("Tie!")
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2's turn

            # Print the board
            print_board(theBoard)

            # Get player 2's choice
            row, col = player_choice(theBoard)

            # Place player 2's marker on the board
            place_marker(theBoard, player2_marker, (row, col))

            # Check if player 2 has won
            if win_check(theBoard, player2_marker):
                print_board(theBoard)
                print("Player 2 wins!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    print_board(theBoard)
                    print("Tie!")
                    break
                else:
                    turn = 'Player 1'

    # Check if players want to play again
    if not replay():
        break
  