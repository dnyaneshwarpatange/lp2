class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find_parent(self, parent, i):
        # Find the parent of the given node 'i'
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        # Perform union of two subsets
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)

        # Attach the smaller rank tree under the root of the higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):

        result = []

        # Sorting the edges based on their weights
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []
        for node in range(self.V):
            # Initialize each node as a separate set
            parent.append(node)
            rank.append(0)

        i, e = 0, 0
        while e < self.V - 1:
            # Get the next edge from the sorted graph
            u, v, w = self.graph[i]
            i += 1

            # Find the parents of the vertices of the edge
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        print("Edges in the minimum spanning tree:")
        for u, v, weight in result:
            print(f"{u} - {v} : {weight}")


# Test the implementation
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 2)
g.add_edge(3, 5, 6)
g.add_edge(4, 5, 3)

g.kruskal_mst()




































# The given code implements the Kruskal's algorithm for finding the minimum spanning tree (MST) of a weighted graph. Here is an explanation of the code:

# 1. The `Graph` class is defined with an initializer that takes the number of vertices as input and initializes an empty graph.

# 2. The `add_edge` method is used to add an edge to the graph. It takes the source vertex (`u`), destination vertex (`v`), and weight (`w`) as input and appends a tuple `(u, v, w)` to the `graph` list.

# 3. The `find_parent` method is a helper function that finds the parent of a given node using the union-find algorithm. It takes a `parent` array and the index `i` of the node as input. It recursively traverses the parent array until it finds the root node (where `parent[i] == i`) and returns the root node.

# 4. The `union` method is another helper function used to perform the union of two subsets. It takes a `parent` array, `rank` array, and two nodes `x` and `y` as input. It first finds the root nodes (`xroot` and `yroot`) of the two subsets using the `find_parent` method. Then it attaches the smaller rank tree under the root of the higher rank tree. If the ranks of the two subsets are equal, the rank of the root node is increased by 1.

# 5. The `kruskal_mst` method is the main function that implements the Kruskal's algorithm to find the MST of the graph. It initializes an empty `result` list to store the edges of the MST. It also sorts the edges of the graph in ascending order of their weights using the `sorted` function and a lambda function as the key.

# 6. It creates an empty `parent` array and a `rank` array to keep track of the subsets and their ranks. It initializes each node as a separate set.

# 7. It initializes variables `i` and `e` to 0. `i` is used to iterate over the sorted edges, and `e` keeps track of the number of edges added to the MST.

# 8. It enters a loop that continues until `e` reaches `V - 1`, where `V` is the number of vertices in the graph. Inside the loop, it gets the next edge from the sorted graph.

# 9. It finds the parent nodes (`x` and `y`) of the vertices (`u` and `v`) of the edge using the `find_parent` method.

# 10. If `x` and `y` are not the same (i.e., they are not in the same subset), it means adding the edge to the MST will not create a cycle. In this case, it increments `e` by 1, appends the edge `(u, v, w)` to the `result` list, and performs the union of the subsets using the `union` method.

# 11. Finally, it prints the edges in the minimum spanning tree by iterating over the `result` list and displaying the source vertex, destination vertex, and weight of each edge.

# 12. The code creates an instance of the `Graph` class, adds edges to the graph using the `add_edge` method, and then calls the `kruskal_mst` method to find and print the minimum spanning tree of the graph.
