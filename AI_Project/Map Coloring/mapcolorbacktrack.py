import time

start_time = time.time()

class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.color_map = {node: None for node in graph}

    def backtracking_search(self):
        return self.recursive_backtracking()

    def recursive_backtracking(self):
        if self.is_complete():
            return self.color_map

        node = self.select_unassigned_variable()
        for color in self.order_domain_values(node):
            if self.is_consistent(node, color):
                self.color_map[node] = color
                result = self.recursive_backtracking()
                if result is not None:
                    return result
                self.color_map[node] = None

        return None

    def is_complete(self):
        return None not in self.color_map.values()

    def select_unassigned_variable(self):
        for node in self.color_map:
            if self.color_map[node] is None:
                return node

    def order_domain_values(self, node):
        return self.colors

    def is_consistent(self, node, color):
        for neighbor in self.graph[node]:
            if self.color_map.get(neighbor) == color:
                return False
        return True
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
color_map = map_coloring.backtracking_search()
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
performance is almost similar, thus, local search would be 
preferable

"""