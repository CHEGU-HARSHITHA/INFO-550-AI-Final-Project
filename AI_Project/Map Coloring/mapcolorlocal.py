import random
import time

start_time = time.time()

class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.color_map = {node: None for node in graph}

    def local_search(self, max_iter=1000):
        self.color_map = self.initial_coloring()

        for i in range(max_iter):
            # Choose a random node
            node = random.choice(list(self.graph.keys()))

            # Choose the color that minimizes conflicts
            min_conflicts = float('inf')
            for color in self.colors:
                conflicts = self.num_conflicts(node, color)
                if conflicts < min_conflicts:
                    min_conflicts = conflicts
                    best_color = color

            # Assign the best color to the node
            self.color_map[node] = best_color

            # If there are no conflicts, return the solution
            if self.num_total_conflicts() == 0:
                return self.color_map

        # If the algorithm reaches the maximum number of iterations, return the best solution found
        return self.color_map

    def initial_coloring(self):
        color_map = {}
        for node in self.graph:
            # Choose a random color for the node
            color_map[node] = random.choice(self.colors)
        return color_map

    def num_conflicts(self, node, color):
        conflicts = 0
        for neighbor in self.graph[node]:
            if self.color_map[neighbor] == color:
                conflicts += 1
        return conflicts

    def num_total_conflicts(self):
        conflicts = 0
        for node in self.graph:
            for neighbor in self.graph[node]:
                if self.color_map[node] == self.color_map[neighbor]:
                    conflicts += 1
        return conflicts // 2  # Divide by 2 to avoid counting each conflict twice

# Example usage
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

colors = ['Red', 'Green', 'Blue']

map_coloring = MapColoring(graph, colors)
color_map = map_coloring.local_search()
print(color_map)

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")

"""
Backtracking search guarantees finding a solution if one exists, 
whereas local search may find a suboptimal solution or get stuck 
in a local optimum. Therefore, if finding an optimal solution is 
critical, or if the search space is very large and complex, 
backtracking search may be a better choice. On the other hand, 
if a good solution is sufficient and the search space is small, 
local search can be a faster and more efficient option. In this 
case, as the search space is small and both the algorithm's 
performance is almost similar, thus local search would be 
preferable
"""
