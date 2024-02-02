# Implement BFS algorithm for topological sort
from queue import Queue

class Graph:
    def __init__(self, v):
        self.vertices=v
        self.adj_list={vertex:[] for vertex in range(self.vertices)}
        self.result=[]
        self.visited = [False] * (self.vertices)

    def addEdge(self, u, v):
        self.adj_list[u].append(v)

    def bfsTopological(self, v):
        q = Queue(maxsize=self.vertices)

        self.visited[v]=True
        q.put(v)

        while q.empty()==False:
            curr=q.get()
            for i in self.adj_list[curr]:
                if self.visited[i]==False:
                    self.visited[i]=True
                    self.result.append(i)
            self.result.append(curr)

    def topological(self):
        
        visited = [False]*(self.vertices)

        for i in range(self.vertices):
            if self.visited[i]==False:
                self.bfsTopological(i)

        print(self.result[::-1])

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(5, 0)

    g.topological()
