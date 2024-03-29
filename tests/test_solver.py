import sys
import os

# Add the parent directory (project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import solver

def test_solve_sudoku():
    board = [
        [0, 0, 0, 6, 7, 0, 0, 5, 0],
        [0, 8, 7, 0, 0, 4, 0, 0, 3],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 2, 1, 0, 5, 0, 0, 3, 0],
        [0, 0, 0, 0, 4, 0, 8, 0, 0],
        [0, 3, 2, 0, 0, 8, 0, 0, 7],
        [0, 9, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    expected_solution = [
        [3, 4, 9, 6, 7, 1, 2, 5, 8],
        [2, 8, 7, 5, 9, 4, 6, 1, 3],
        [1, 6, 5, 2, 8, 3, 4, 7, 9],
        [4, 5, 8, 7, 3, 6, 9, 2, 1],
        [9, 7, 3, 4, 1, 2, 5, 8, 6],
        [6, 2, 1, 8, 5, 9, 7, 3, 4],
        [7, 1, 6, 3, 4, 5, 8, 9, 2],
        [5, 3, 2, 9, 6, 8, 1, 4, 7],
        [8, 9, 4, 1, 2, 7, 3, 6, 5]
    ]
    
    solver.solve_sudoku(board)
    assert board == expected_solution
