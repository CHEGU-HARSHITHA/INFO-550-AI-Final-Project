import time

start_time = time.time()

def solve_n_queens(n):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        n: the number of queens and size of the board.

    Returns:
        A tuple of two lists of solutions:
        - The first list contains solutions in column_positions format (e.g. [(1, 3, 0, 2), (2, 0, 3, 1)])
        - The second list contains solutions in matrix format (e.g. [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]])
    """
    # Initialize empty lists to store solutions
    column_positions_solutions = []
    matrix_solutions = []

    # Create an empty board
    board = [[0] * n for _ in range(n)]

    # Define a helper function to check if a placement is valid
    def is_valid(row, col):
        # Check row and column
        for i in range(n):
            if board[i][col] == 1 or board[row][i] == 1:
                return False
        # Check diagonals
        for i in range(n):
            for j in range(n):
                if i + j == row + col or i - j == row - col:
                    if board[i][j] == 1:
                        return False
        return True

    # Define a recursive backtracking function
    def backtrack(row):
        # Base case: all queens have been placed
        if row == n:
            # Add the current solution to the list of solutions
            column_positions_solution = tuple([board[i].index(1) for i in range(n)])
            column_positions_solutions.append(column_positions_solution)
            matrix_solutions.append([row[:] for row in board])
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            # Check if the placement is valid
            if is_valid(row, col):
                # Place the queen
                board[row][col] = 1
                # Recursively try to place the remaining queens
                backtrack(row + 1)
                # Remove the queen (backtrack)
                board[row][col] = 0

    # Start the backtracking algorithm from the first row
    backtrack(0)

    
    return column_positions_solutions, matrix_solutions

column_positions_solutions, matrix_solutions = solve_n_queens(4)
print(column_positions_solutions)
print(matrix_solutions)

end_time = time.time()

print("Execution time:", end_time - start_time, "seconds")

"""
The local search approach is generally faster than the backtracking 
search approach for large values of n, as it has a lower time complexity. 
However, backtracking search may be preferable for smaller values of n 
or when a complete set of solutions is desired. Additionally, local 
search is more suited to finding a single solution, while backtracking 
can find all possible solutions
"""