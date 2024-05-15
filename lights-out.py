# Lights out represents 0
# Lights in represents 1

GRID_ROW = 3
GRID_COL = 3

def start_board(n, m):
    init_board = []
    for i in range(n):
        init_board.append([1 for _ in range(m)])
    return init_board

def main():
    board_row = int(input("Width of the board: "))
    board_col = int(input("Height of the board: "))
    initial_board = start_board(board_row, board_col)
    while True:
        print("Enter the grid block to toggle between 1 and 3")
        row = int(input("What row do you want to toggle: "))
        col = int(input("What column do you want to toggle: "))
        # Check the first toggled value
        if initial_board[row - 1][col - 1] == 1:
            initial_board[row - 1][col - 1] = 0
            # Check the top of the toggled value
            # Still the same column but one row before
            if row - 2 >= 0:
                if initial_board[row - 2][col - 1] == 1:
                    initial_board[row - 2][col - 1] = 0
                else:
                    initial_board[row - 2][col - 1] = 1
            # Check the bottom of the toggled value row-wise
            if row <= 2:
                if initial_board[row][col - 1] == 1:
                    initial_board[row][col - 1] = 0
                else:
                    initial_board[row][col - 1] = 1
            # Check the left hand neighbor of the toggled value
            if col - 2 >= 0:
                if initial_board[row - 1][col - 2] == 1:
                    initial_board[row - 1][col - 2] = 0
                else:

                    initial_board[row - 1][col - 2] = 1
            # Check the right hand neigbor of the toggled value
            if col <= 2:
                if initial_board[row - 1][col] == 1:
                    initial_board[row - 1][col] = 0
                else:
                    initial_board[row - 1][col] = 1
        else:
            initial_board[row - 1][col - 1] = 1

            # Check the top of the toggled value
            # Still the same column but one row before
            if row - 2 >= 0:
                if initial_board[row - 2][col - 1] == 1:
                    initial_board[row - 2][col - 1] = 0
                else:
                    initial_board[row - 2][col - 1] = 1
            # Check the bottom of the toggled value row-wise
            if row <= 2:
                if initial_board[row][col - 1] == 1:
                    initial_board[row][col - 1] = 0
                else:
                    initial_board[row][col - 1] = 1
            # Check the left hand neighbor of the toggled value
            if col - 2 >= 0:
                if initial_board[row - 1][col - 2] == 1:
                    initial_board[row - 1][col - 2] = 0
                else:

                    initial_board[row - 1][col - 2] = 1
            # Check the right hand neigbor of the toggled value
            if col <= 2:
                if initial_board[row - 1][col] == 1:
                    initial_board[row - 1][col] = 0
                else:
                    initial_board[row - 1][col] = 1

        zero_count = 0
        for i in range(board_row):
            for j in range(board_col):
                if initial_board[i][j] == 0:
                    zero_count += 1
                print(initial_board[i][j], end=' ')
            print()


        if zero_count == (board_col * board_row):
            print('Game won. The game has ended')
            break



if __name__ == '__main__':
    main()