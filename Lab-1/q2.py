class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in range(1, vertices + 1)}
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, start, end):
        # Adding edge to the adjacency list
        self.adj_list[start].append(end)
        self.adj_list[end].append(start)

        # Adding edge to the adjacency matrix
        self.adj_matrix[start - 1][end - 1] = 1
        self.adj_matrix[end - 1][start - 1] = 1

    def display_adj_list(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")

    def display_adj_matrix(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)


# Create a graph with vertices {1, 2, 3, 4}
graph = Graph(4)

# Add edges to the graph
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

# Display the adjacency list and adjacency matrix
graph.display_adj_list()
print()
graph.display_adj_matrix()
