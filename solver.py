board = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
         [2, 8, 9, 0, 0, 4, 0, 0, 0],
         [3, 4, 6, 2, 0, 5, 0, 9, 0],
         [6, 0, 2, 0, 0, 0, 0, 1, 0],
         [0, 3, 8, 0, 0, 6, 0, 4, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 7, 8],
         [7, 0, 3, 4, 0, 0, 5, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def validator(row, col, matrix):
    valid = 0
    for number in range(1, 10):
        # Check if the number is not in the col/row/matrix[3*3].
        if number not in row and number not in col and number not in matrix:
            valid_number = number
            valid += 1
    # Check if there is only one number that can match.
    if valid == 1:
        return valid_number
    else:
        return False


def start(board):
    count = -1
    for row in board:
        for col in row:
            count += 1
            if col == 0:
                col_list = []
                matrix = []
                current_row = int(count / len(row))
                current_col = int(count % 9)
                strat_row = current_row - (current_row % 3)
                strat_col = current_col - (current_col % 3)
                for x in range(3):
                    for y in range(3):
                        matrix.append(board[strat_row + x][strat_col + y])
                for i in range(len(row)):
                    col_list.append(board[i][current_col])
                check = validator(row, col_list, matrix)
                if check:
                    board[current_row][current_col] = check
    return board


start(board)
print("---- This is first try -----")
print_board(board)
tried = 1

# Check if the sudoku is solved.
while any(0 in row for row in board):
    start(board)
    tried += 1
    print("---- This is try number", tried, "-----")
    print_board(board)
