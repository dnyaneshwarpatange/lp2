class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.num_vertices = len(graph)
        self.solution = [-1] * self.num_vertices

    def is_safe(self, vertex, color):
        for neighbor in range(self.num_vertices):
            if self.graph[vertex][neighbor] == 1 and self.solution[neighbor] == color:
                return False
        return True

    def solve_graph_coloring(self, vertex):
        if vertex == self.num_vertices:
            return True

        for color in self.colors:
            if self.is_safe(vertex, color):
                self.solution[vertex] = color

                if self.solve_graph_coloring(vertex + 1):
                    return True

                self.solution[vertex] = -1

        return False

    def solve(self):
        if self.solve_graph_coloring(0):
            print("Solution exists:")
            for vertex, color in enumerate(self.solution):
                print("Vertex", vertex, "-> Color", color)
        else:
            print("No solution exists.")


# Example usage
graph = [[1, 0, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
        [0, 1, 1, 1]]

colors = [1, 2, 3]  # Available colors

graph_coloring = GraphColoring(graph, colors)
graph_coloring.solve()





# The code defines a class called GraphColoring with an initialization method (__init__). It takes a graph and a list of colors as input and initializes various attributes of the class.

# The is_safe method checks if it is safe to assign a particular color to a given vertex. It iterates over all the neighbors of the vertex and checks if any of them have been assigned the same color. If a neighbor has the same color, it returns False, indicating it is not safe to assign that color to the vertex. Otherwise, it returns True.

# The solve_graph_coloring method is a recursive function that solves the graph coloring problem. It takes a vertex parameter representing the current vertex being processed. If the vertex is equal to the total number of vertices in the graph (self.num_vertices), it means all vertices have been processed, and a valid solution has been found. In that case, it returns True.

# Inside the solve_graph_coloring method, there is a loop that iterates over all the available colors. For each color, it checks if it is safe to assign that color to the current vertex using the is_safe method. If it is safe, it assigns the color to the vertex in the self.solution list.

# After assigning the color, the solve_graph_coloring method calls itself recursively with the next vertex (vertex + 1). If the recursive call returns True, it means a solution has been found, and it returns True to the previous recursive call.

# If the recursive call does not return True, it means the current color assignment is not part of the solution, so the color is reset to -1 (indicating no color assigned) in the self.solution list.

# After the loop, if no color assignment leads to a valid solution, the solve_graph_coloring method returns False.

# The solve method is called to solve the graph coloring problem. It calls the solve_graph_coloring method with the initial vertex (0). If a solution is found, it prints the vertex-color assignments. Otherwise, it prints that no solution exists.

# In the example usage, a graph and a list of colors are defined. The GraphColoring class is instantiated with the graph and colors. Then, the solve method is called to find a solution to the graph coloring problem