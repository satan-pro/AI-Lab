class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in range(0, vertices)}

    def add_edge(self, start, end):
        # Adding edge to the adjacency list
        self.adj_list[start].append(end)
        #self.adj_list[end].append(start)


    def display_adj_list(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")


# Create a graph with vertices {0,1, 2, 3, 4,5}
graph = Graph(6)

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(4, 5)
graph.add_edge(5, 4)

# Display the adjacency list and adjacency matrix
graph.display_adj_list()

