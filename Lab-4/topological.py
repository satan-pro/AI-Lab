from queue import Queue

class Graph: 
    def __init__(self, v):
        self.vertices=v
        self.adj_list = {vertex:[] for vertex in range(self.vertices)}
        self.result=[]

    def addEdge(self , src, dest):
        self.adj_list[dest].append(src)

    def topological(self):

        for i in self.adj_list:
            if len(self.adj_list[i])==0:
                self.result.append(i)
                

        print(self.result)

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(5, 0)

    g.topological()