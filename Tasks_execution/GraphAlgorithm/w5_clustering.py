#Uses python3
import sys
import math
import numpy as np

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

def clustering(n, x, y, k):
    X, lengths = Kruskal(n, x, y)
    x = X[-(k-1)]    
    return lengths[x]


    #input = sys.stdin.read()
    #input = "12 7 6 4 3 5 1 1 7 2 7 5 7 3 3 7 8 2 8 4 4 6 7 2 6 3" # 2.828427124746
    input = "8 3 1 1 2 4 6 9 8 9 9 8 9 3 11 4 12 4" # 5.000000000

    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]

    print("{0:.9f}".format(clustering(n, x, y, k)))
