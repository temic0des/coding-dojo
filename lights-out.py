# Lights out represents 0
# Lights in represents 1

GRID_ROW = 3
GRID_COL = 3

def main():
    initial_board = [[0, 1, 0], [0, 0, 0], [1, 1, 0]]
    while True:
        print("Enter the grid block to toggle between 1 and 3")
        row = int(input("What row do you want to toggle: "))
        col = int(input("What column do you want to toggle: "))
        # Check the first toggled value
        if initial_board[row - 1][col - 1] == 1:
            initial_board[row - 1][col - 1] = 0
            # Check the top of the toggled value
            # Still the same column but one row before
            if row - (GRID_ROW - 1) >= 0:
                if initial_board[row - 2][col - 1] == 1:
                    initial_board[row - 2][col - 1] = 0
                else:
                    initial_board[row - 2][col - 1] = 1
            # Check the bottom of the toggled value row-wise
            if row <= GRID_ROW - 1:
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
            if col <= GRID_COL - 1:
                if initial_board[row - 1][col] == 1:
                    initial_board[row - 1][col] = 0
                else:
                    initial_board[row - 1][col] = 1
        else:
            initial_board[row - 1][col - 1] = 1

            # Check the top of the toggled value
            # Still the same column but one row before
            if row - (GRID_ROW - 1) >= 0:
                if initial_board[row - 2][col - 1] == 1:
                    initial_board[row - 2][col - 1] = 0
                else:
                    initial_board[row - 2][col - 1] = 1
            # Check the bottom of the toggled value row-wise
            if row <= GRID_ROW - 1:
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
            if col <= GRID_COL - 1:
                if initial_board[row - 1][col] == 1:
                    initial_board[row - 1][col] = 0
                else:
                    initial_board[row - 1][col] = 1

        zero_count = 0
        for i in range(GRID_ROW):
            for j in range(GRID_COL):
                if initial_board[i][j] == 0:
                    zero_count += 1
                print(initial_board[i][j], end=' ')
            print()

        if zero_count == 9:
            print('Game won. The game has ended')
            break



if __name__ == '__main__':
    main()