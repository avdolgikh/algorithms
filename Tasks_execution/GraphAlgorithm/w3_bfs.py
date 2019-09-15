#Uses python3

import sys
from queue import Queue

class BreadthFirstSearch:
    def run(self, adjacency_matrix, origin_vertex):
        n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.dist = [-1] * n
        self.prev = [-1] * n
        self.dist[origin_vertex] = 0
        self.Q = Queue()
        self.Q.put(origin_vertex)

        while not self.Q.empty():
            u = self.Q.get()
            for v in self.adjacency_matrix[u]:
                if self.dist[v] == -1:
                    self.Q.put(v)
                    self.dist[v] = self.dist[u] + 1
                    self.prev[v] = u

def distance(adj, s, t):
    bfs = BreadthFirstSearch()
    bfs.run(adj, s)
    return bfs.dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    s, t = data[2 * m] - 1, data[2 * m + 1] - 1

    print(distance(adj, s, t))
