import time

def solve_sudoku(board):

    # Keep a global count of how many times the function is called
    global num_calls
    num_calls += 1

    # Check if there are any empty cells left
    if not find_empty_cell(board):
        return True

    # Find the coordinates of an empty cell
    row, col = find_empty_cell(board)

    # Try numbers from 1 to 9 for the empty cell
    for num in range(1, 10):
        # Check if the number is a valid move
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            # Perform forward checking to eliminate invalid moves
            if forward_checking(board, row, col):
                # Recursively call solve_sudoku function
                if solve_sudoku(board):
                    return True

            # Reset the cell to empty (0) if the move is not valid
            board[row][col] = 0

    # If no valid move is found, backtrack to the previous cell and try a different number
    return False


def find_empty_cell(board):

    # Loop through all the cells in the board
    for row in range(9):
        for col in range(9):
            # If a cell is empty (i.e., its value is 0), return its indices
            if board[row][col] == 0:
                return (row, col)
    # If no empty cells are found in the board, return None
    return None

def is_valid_move(board, row, col, num):

    # Check if the same number exists in the same row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the same number exists in the same 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    
    # If the number doesn't violate any of the rules, return True
    return True

def forward_checking(board, row, col):
    # Loop over the rows and columns to check if the board has a valid move. If there is an empty cell and there is no valid move, return False
    for i in range(9):
        if board[row][i] == 0:
            if not has_valid_move(board, row, i):
                return False

        if board[i][col] == 0:
            if not has_valid_move(board, i, col):
                return False

    # Calculate the box where the cell belongs to
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    # Loop over the cells in the box to check if the board has a valid move. If there is an empty cell and there is no valid move, return False
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == 0:
                if not has_valid_move(board, box_row + i, box_col + j):
                    return False

    # If there is a valid move for all empty cells, return True
    return True

def has_valid_move(board, row, col):
    # Loop over the possible values to see if there is a valid move
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            return True
    return False


#Define the grids
#Grids are taken from Sudoku, a mobile gaming application
simple_grid = [    [8, 0, 6, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 5, 0, 4],
    [4, 5, 9, 0, 0, 0, 1, 8, 0],
    [3, 9, 0, 2, 0, 0, 7, 5, 0],
    [7, 6, 8, 4, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 9, 4, 6],
    [6, 8, 2, 0, 9, 0, 0, 7, 0],
    [0, 0, 1, 5, 6, 7, 8, 3, 2],
    [0, 7, 3, 0, 2, 4, 0, 0, 0]
]

medium_grid = [    [0, 0, 0, 8, 0, 0, 0, 3, 0],
    [9, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 4, 0, 5, 0, 0, 2, 0],
    [0, 4, 7, 0, 0, 6, 0, 5, 0],
    [3, 2, 6, 0, 0, 0, 4, 8, 1],
    [0, 5, 0, 2, 0, 0, 6, 7, 0],
    [0, 9, 0, 0, 4, 0, 3, 0, 0],
    [0, 0, 5, 0, 0, 0, 0, 0, 7],
    [0, 6, 0, 0, 0, 7, 0, 0, 0]
]

hard_grid = [    [0, 0, 9, 0, 7, 5, 0, 0, 0],
    [0, 1, 8, 3, 0, 0, 0, 0, 0],
    [3, 5, 0, 0, 0, 0, 0, 9, 0],
    [6, 0, 0, 0, 0, 8, 7, 2, 0],
    [0, 0, 5, 0, 0, 0, 9, 0, 0],
    [0, 9, 7, 6, 0, 0, 0, 0, 3],
    [0, 2, 0, 0, 0, 0, 0, 1, 9],
    [0, 0, 0, 0, 0, 4, 5, 7, 0],
    [0, 0, 0, 1, 5, 0, 8, 0, 0]
]

num_calls = 0
start_time = time.time()
if solve_sudoku(simple_grid):
    elapsed_time = time.time() - start_time
    print("Solution found for simple grid in {:.3f} seconds:".format(elapsed_time))
    # If a solution is found, print the solved puzzle
    for row in simple_grid:
        print(row)
else:
    print("No solution found.")
print("Number of recursive calls:", num_calls)

num_calls = 0
start_time = time.time()
if solve_sudoku(medium_grid):
    elapsed_time = time.time() - start_time
    print("Solution found for medium grid in {:.3f} seconds:".format(elapsed_time))
    # If a solution is found, print the solved puzzle
    for row in medium_grid:
        print(row)
else:
    print("No solution found.")
print("Number of recursive calls:", num_calls)

num_calls = 0
start_time = time.time()
if solve_sudoku(hard_grid):
    elapsed_time = time.time() - start_time
    print("Solution found for hard grid in {:.3f} seconds:".format(elapsed_time))
    # If a solution is found, print the solved puzzle
    for row in hard_grid:
        print(row)
else:
    print("No solution found.")
print("Number of recursive calls:", num_calls)

"""
I ran two Sudoku solvers, one using backtracking search and 
another using backtracking search with forward checking. 
Both solvers are able to correctly solve all three input 
Sudoku puzzles of varying difficulties. The solver with 
forward checking performed better in terms of the number 
of recursive calls required and had a slightly faster 
execution time. Backtracking with forward checking is 
preferable over simple backtracking when there are many 
constraints in the problem and the domain of each variable 
is large. Forward checking helps reduce the search space by 
eliminating values that cannot be used in the future, thus 
increasing efficiency. Additionally, forward checking can 
help detect failure earlier in the search process. 
However, it comes with the cost of additional computational 
overhead.

"""