def print_board(board):
    for row in board:
        print(*row)


def is_valid(board, row, col, num):
    # Check if the number is not present in the same row
    if num in board[row]:
        return False

    # Check if the number is not present in the same column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is not present in the same 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True
