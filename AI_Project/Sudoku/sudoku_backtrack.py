import time

def solve_sudoku(grid):
    """
    Solving a Sudoku puzzle using backtracking search.

    Args:
        grid: a 2D array representing the Sudoku puzzle, where 0 represents an empty cell.

    Returns:
        True if a solution is found, False otherwise.
    """
    
    global num_calls
    num_calls += 1

    # Find an empty cell in the grid
    cell = find_empty_cell(grid)

    # If there are no more empty cells, the puzzle is solved
    if not cell:
        return True

    row, col = cell

    # Try assigning each value from 1 to 9 to the empty cell
    for val in range(1, 10):
        # Check if the assignment violates any constraints
        if is_valid_assignment(grid, row, col, val):
            # Assign the value to the empty cell
            grid[row][col] = val

            # Recursively try to solve the remaining puzzle
            if solve_sudoku(grid):
                return True

            # If the recursive call fails, backtrack by resetting the cell to 0
            grid[row][col] = 0

        

    # If all possible values have been tried and none of them work, the puzzle is unsolvable
    return False

def find_empty_cell(grid):
    """
    Find the next empty cell in the Sudoku grid.
    Returns a tuple of (row, col), or None if no empty cells are found.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None


def is_valid_assignment(grid, row, col, val):
    """
    Check if assigning a value to a cell in the grid violates any constraints.

    Args:
        grid: a 2D array representing the Sudoku puzzle.
        row: the row of the cell to assign a value to.
        col: the column of the cell to assign a value to.
        val: the value to assign to the cell.

    Returns:
        True if the assignment is valid, False otherwise.
    """
    # Check row constraint
    if val in grid[row]:
        return False

    # Check column constraint
    if val in [grid[i][col] for i in range(9)]:
        return False

    # Check subgrid constraint
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    if val in [grid[subgrid_row + i][subgrid_col + j] for i in range(3) for j in range(3)]:
        return False

    return True


#Define the sudoku grids
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
    #Print the time taken to solve the puzzle
    print("Solution found for simple grid in {:.3f} seconds:".format(elapsed_time))
    # If a solution is found, print the solved puzzle
    for row in simple_grid:
        print(row)
else:
    print("No solution found.")
#Print the number of recursive calls taken
print("Number of recursive calls:", num_calls)

num_calls = 0
start_time = time.time()
if solve_sudoku(medium_grid):
    elapsed_time = time.time() - start_time
    #Print the time taken to solve the puzzle
    print("Solution found for medium grid in {:.3f} seconds:".format(elapsed_time))
    # If a solution is found, print the solved puzzle
    for row in medium_grid:
        print(row)
else:
    print("No solution found.")
#Print the number of recursive calls taken
print("Number of recursive calls:", num_calls)

num_calls = 0
start_time = time.time()
if solve_sudoku(hard_grid):
    elapsed_time = time.time() - start_time
    #Print the time taken to solve the puzzle
    print("Solution found for hard grid in {:.3f} seconds:".format(elapsed_time))
    # If a solution is found, print the solved puzzle
    for row in hard_grid:
        print(row)
else:
    print("No solution found.")
#Print the number of recursive calls taken
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