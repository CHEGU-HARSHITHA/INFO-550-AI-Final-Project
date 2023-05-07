import random
import time

start_time = time.time()

def conflicts(var, value, assignment, n):
    """
    Counts the number of conflicts with other queens if the given variable is assigned the given value.
    """
    count = 0
    for i in range(n):
        if i != var and (value == assignment[i] or abs(var-i) == abs(value-assignment[i])):
            count += 1
    return count

def min_conflicts(n):
    """
    Solves the n queens problem using the MIN-CONFLICTS heuristic.
    """
    # Initialize the assignment randomly
    assignment = [random.randint(0, n-1) for i in range(n)]
    while True:
        # Check if the current assignment is a solution
        if sum(conflicts(var, assignment[var], assignment, n) for var in range(n)) == 0:
            return assignment
        # Choose a random conflicted variable
        var = random.choice([i for i in range(n) if conflicts(i, assignment[i], assignment, n) > 0])
        # Choose the value that minimizes the number of conflicts
        values = [(value, conflicts(var, value, assignment, n)) for value in range(n)]
        min_conflicts = min(values, key=lambda x: x[1])[1]
        best_values = [value for value, conflicts in values if conflicts == min_conflicts]
        value = random.choice(best_values)
        assignment[var] = value
    return None

print(min_conflicts(4))

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