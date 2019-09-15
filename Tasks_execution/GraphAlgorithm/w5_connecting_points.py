#Uses python3
import sys
import math
import numpy as np
import heapq

class DisjointSets:
    def __init__(self, size):
        self.parent = [0] * size
        self.rank = [0] * size

    def make_set(self, i):
        self.parent[i] = i
        self.rank[i] = 0

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        
        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1

def Kruskal(n, x, y):
    edges = []
    edge_lengths = []
    for i in range(n-1):
        for j in range(i+1, n):
            edges.append( (i, j) )
            edge_lengths.append( math.sqrt( (x[i] - x[j])**2 + (y[i] - y[j])**2 ) )
    sorted_edge_indices = np.argsort(edge_lengths)

    ds = DisjointSets(n)
    for u in range(n):
        ds.make_set(u)
    
    X = [] # edge indices with shortest total length

    for i in sorted_edge_indices:
        (u, v) = edges[i]
        if ds.find(u) != ds.find(v):
            X.append(i)
            ds.union(u, v)

    return X, edge_lengths

def Prim(n, x, y):
    costs = [np.inf] * n
    parent = [-1] * n
    visited = [0] * n

    u_0 = 0 # pick any initial vertex
    costs[u_0] = 0

    heap = [(costs[i], i) for i in range(n)]
    heapq.heapify(heap)

    while len(heap) > 0:
        v = heapq.heappop(heap)[1]
        if visited[v] == 0:
            visited[v] = 1
            for z in range(n):
                if visited[z] == 0:
                    weight = math.sqrt( (x[v] - x[z])**2 + (y[v] - y[z])**2 )
                    if costs[z] > weight:
                        costs[z] = weight
                        parent[z] = v
                        heapq.heappush(heap, (costs[z], z))
    return costs


def minimum_distance(n, x, y):
    X, lengths = Kruskal(n, x, y)
    result = sum( lengths[i] for i in X )
    return result

def minimum_distance_p(n, x, y):
    costs = Prim(n, x, y)
    result = sum( costs )
    return result


if __name__ == '__main__':
    #input = sys.stdin.read()
    input = "5 0 0 0 2 1 1 3 0 3 2"
    #input = "4 0 0 0 1 1 0 1 1"

    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    print("{0:.9f}".format(minimum_distance(n, x, y)))
    print("{0:.9f}".format(minimum_distance_p(n, x, y)))
