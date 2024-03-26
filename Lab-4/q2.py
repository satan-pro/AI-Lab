
import math
import sys
from collections import defaultdict


class Graph:
	def __init__(self,vertices):
		self.graph=defaultdict(list)
		self.V=vertices 
	

	def addEdge(self,u,v):
		self.graph[u].append(v)


def isCycleExist(n,graph):
	in_degree=[0]*n

	for i in range(n):
		for j in graph[i]:
			in_degree[j]+=1
	
	queue=[]
	for i in range(len(in_degree)):
		if in_degree[i]==0:
			queue.append(i)
	
	cnt=0
	# One by one dequeue vertices from queue and enqueue 
	# adjacents if indegree of adjacent becomes 0 
	while(queue):

		# Extract front of queue (or perform dequeue) 
		# and add it to topological order 
		nu=queue.pop(0)

		# Iterate through all its neighbouring nodes 
		# of dequeued node u and decrease their in-degree 
		# by 1 
		for v in graph[nu]:
			in_degree[v]-=1

			# If in-degree becomes zero, add it to queue
			if in_degree[v]==0:
				queue.append(v)
		cnt+=1

	# Check if there was a cycle 
	if cnt==n:
		return False
	else:
		return True
		


if __name__=='__main__':

	g=Graph(4)
	g.addEdge(0,1)
	g.addEdge(1,2)
	g.addEdge(2,3)
	'''g.addEdge(3,3)
	g.addEdge(2,3)
	g.addEdge(0,2)'''

	if isCycleExist(g.V,g.graph):
		print("Cycle Exists")
	else:
		print("Acyclic Graph")


