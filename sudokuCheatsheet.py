import numpy as np 

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, or 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # Check the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
                
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Temporarily assign the number
                        
                        if solve_sudoku(board):  # Recur to fill the rest
                            return True
                        
                        board[row][col] = 0  # Backtrack if no solution found
                
                return False  # No valid number was found for this cell
    
    return True  # All cells filled

def print_board(board):
    for row in board:
        print(row)

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [3, 0, 0, 0, 0, 6, 2, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 6, 0, 5],
    [0, 2, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 7, 9, 0, 0, 4, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 8],
    [2, 5, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 1, 0, 0, 0, 0, 0],
    [0, 0, 3, 8, 0, 4, 0, 0, 0]
]

if solve_sudoku(sudoku_board):
    print("Sudoku solved successfully:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
