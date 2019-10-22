import numpy as np
import sys
from src.queue import Queue

class Graph(object):
    def __init__(self):
        self.V = [str(i) for i in range(1,9)]
        self.E = {
            '1': {'2':1, '5':1},
            '2': {'1':1, '6':1},
            '3': {'4':1, '6':1, '7':1},
            '4': {'3':1, '7':1, '8':1},
            '5': {'1':1},
            '6': {'2':1, '3':1, '7':1},
            '7': {'3':1, '4':1, '6':1, '8':1},
            '8': {'4':1, '7':1}
        }
    
    def bfs(self, s):
        # initialize
        visited, distance, parent = {}, {}, {}
        for v in self.V:
            visited[v] = 0
            distance[v] = np.NaN
            parent[v] = None

        distance[s] = 0
        
        # keep a Queue for un-visited nodes
        q = Queue()
        q.enqueue(s)
        
        while not q.isempty():
            u = q.dequeue()
            print(u, parent[u], distance[u])
            visited[u] = 1
            for v in self.E[u].keys():
                if not visited[v]:
                    visited[v] = 1
                    distance[v] = distance[u] + self.E[u][v]
                    parent[v] = u
                    q.enqueue(v)

    def dfs(self, s):
        visited, parent = {}, {}
        for v in self.V:
            visited[v] = 0
            parent[v] = None
        self._dfs_visit(s, visited, parent)
    
    def _dfs_visit(self, u, visited, parent):
        print(u, parent[u])
        visited[u] = 1
        for v in self.E[u].keys():
            if not visited[v]:
                parent[v] = u
                self._dfs_visit(v, visited, parent)
    
    def _min_distance(self, d, visited):
        minval = sys.maxsize
        minnode = self.V[0]
        for w in self.V:
            if not visited[w] and d[w] < minval:
                minval = d[w]
                minnode = w
        return minnode
    
    def prim_mst(self, s):
        visited, distance, parent = {}, {}, {}
        for v in self.V:
            visited[v] = 0
            distance[v] = sys.maxsize
            parent[v] = None
        
        distance[s] = 0
        
        for v in self.V:
            u = self._min_distance(distance, visited)
            print(u, parent[u], distance[u])
            visited[u] = 1
            for v in self.E[u].keys():
                if not visited[v] and distance[v] > self.E[u][v]:
                    distance[v] = self.E[u][v]
                    parent[v] = u

    def dijkstra(self, s):        
        visited, distance = {}, {}
        for v in self.V:
            visited[v] = 0
            distance[v] = sys.maxsize
        
        distance[s] = 0
        
        for v in self.V:
            u = self._min_distance(distance, visited)
            print(u, distance[u])
            visited[u] = 1
            for v in self.E[u].keys():
                if not visited[v] and distance[v] > distance[u] + self.E[u][v]:
                    distance[v] = distance[u] + self.E[u][v]
