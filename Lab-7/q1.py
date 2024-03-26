class Graph:
    def __init__(self, v):
        self.vertices=v
        self.adjList={vertex: [] for vertex in range(0, v)}

    def addEdge(self, src, dest, wt):
        self.adjList[src].append((dest, wt))

    
