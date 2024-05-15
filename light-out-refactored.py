
def start_board(n, m):
    init_board = []
    for i in range(n):
        init_board.append([1 for _ in range(m)])
    return init_board


def print_board(board, n, m):
    for i in range(m):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def positive_input(text, m, n):
    try:
        number = int(input(text))
        return number
    except ValueError:
        pass

def toggle_checked_value(board, row, col, n):
    if board[row - 1][col - 1] == 1:
        board[row - 1][col - 1] = 0
        toggle_top_of_checked_value(board, row, col)
        toggle_bottom_of_checked_value(board, row, col, n)
        toggle_left_of_checked_value(board, row, col)
        toggle_right_of_checked_value(board, row, col)
    else:
        board[row - 1][col - 1] = 1
        toggle_top_of_checked_value(board, row, col)
        toggle_bottom_of_checked_value(board, row, col, n)
        toggle_left_of_checked_value(board, row, col)
        toggle_right_of_checked_value(board, row, col)

def toggle_top_of_checked_value(board, row, col):
    if row - 1 > 0:
        if board[row - 2][col - 1] == 1:
            board[row - 2][col - 1] = 0
        else:
            board[row - 2][col - 1] = 1

def toggle_bottom_of_checked_value(board, row, col, n):
    if row > n:
        print(row)
        if board[row][col - 1] == 1:
            board[row][col - 1] = 0
        else:
            board[row][col - 1] = 1

def toggle_left_of_checked_value(board, row, col):
    if col - 1 > 0:
        if board[row - 1][col - 2] == 1:
            board[row - 1][col - 2] = 0
        else:
            board[row - 1][col - 2] = 1

def toggle_right_of_checked_value(board, row, col):
    if col < 1:
        if board[row - 1][col] == 1:
            board[row - 1][col] = 0
        else:
            board[row - 1][col] = 1




def main():
    board_row = int(input("Width of the board: "))
    board_col = int(input("Height of the board: "))
    initial_board = start_board(board_row, board_col)
    initial_board = [[1, 0, 1], [1, 0, 0], [1, 0, 0]]
    # initial_board = [[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 1, 1, 0, 1]]
    print_board(initial_board, m=board_row, n=board_col)
    while True:
        print(f"Enter the grid block to toggle between 1 and {board_row}")
        row = int(input("What row do you want to toggle: "))
        col = int(input("What column do you want to toggle: "))
        toggle_checked_value(initial_board, row=row, col=col, n=board_row)

        print_board(board=initial_board, m=board_row, n=board_col)

if __name__ == '__main__':
    main()