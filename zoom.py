def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def get_user_input(player):
    row = int(input(f"{player}, enter row (1-3): ")) - 1
    col = int(input(f"{player}, enter column (1-3): ")) - 1
    return row, col

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    for condition in win_conditions:
        if all(cell == player for cell in condition):
            return True
    return False

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        row, col = get_user_input(player)
        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Cell already taken. Choose another one.")
            continue

        if check_win(board, player):
            print_board(board)
            print(f"{player} wins!")
            break

        player = 'O' if player == 'X' else 'X'

        if all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
