import sys

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

	def printSolution(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])

	def minDistance(self, dist, sptSet):

		min = sys.maxsize

		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index

	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			x = self.minDistance(dist, sptSet)
			sptSet[x] = True

			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]

		self.printSolution(dist)

if __name__ == "__main__":
	g = Graph(9)
	g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
			[4, 0, 8, 0, 0, 0, 0, 11, 0],
			[0, 8, 0, 7, 0, 4, 0, 0, 2],
			[0, 0, 7, 0, 9, 14, 0, 0, 0],
			[0, 0, 0, 9, 0, 10, 0, 0, 0],
			[0, 0, 4, 14, 10, 0, 2, 0, 0],
			[0, 0, 0, 0, 0, 2, 0, 1, 6],
			[8, 11, 0, 0, 0, 0, 1, 0, 7],
			[0, 0, 2, 0, 0, 0, 6, 7, 0]
			]

	g.dijkstra(0)







































# Create a class Graph with necessary methods and variables to represent the graph. In this case, the code snippet defines a Graph class with a constructor that initializes the number of vertices (V) and an adjacency matrix (graph) to store the weights between vertices.

# Implement a method to find the minimum distance in the graph. In the given code, the method minDistance finds the vertex with the minimum distance that has not been included in the minimum spanning tree yet.

# Implement the Kruskal algorithm in the dijkstra method. Initialize an empty set (sptSet) to store the vertices included in the MST and an array (dist) to store the minimum distance from the source vertex to each vertex.

# Iterate V times, where V is the number of vertices in the graph. In each iteration, find the vertex with the minimum distance that has not been included in sptSet using the minDistance method.

# Add the selected vertex to sptSet and update the distance of its adjacent vertices if the new distance is smaller. In the given code, this is done by checking the conditions if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]. If the conditions are satisfied, update dist[y] with the new distance.

# After the iterations are complete, the printSolution method is called to print the vertex and its corresponding distance from the source.

# In the main block, a Graph object is created with 9 vertices. The adjacency matrix is initialized with the weights between vertices.

# Finally, the dijkstra method is called on the Graph object with a source vertex of 0 to find the shortest paths from the source to all other vertices.