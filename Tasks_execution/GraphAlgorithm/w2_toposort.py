#Uses python3

import sys

class DepthFirstSearch:
    def run(self, adjacency_matrix):
        n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.visited = [0] * n
        self.pre = [0] * n
        self.post = [0] * n
        self.clock = 1
        self.postordered_vertices = []

        for v in range(n):
            if self.visited[v] == 0:
                self.explore(v)

    def explore(self, v):
        self.visited[v] = 1
        self.previsit(v)
        for u in self.adjacency_matrix[v]:
            if self.visited[u] == 0:
                self.explore(u)
        self.postvisit(v)

    def previsit(self, v):
        self.pre[v] = self.clock
        self.clock += 1
    
    def postvisit(self, v):
        self.post[v] = self.clock
        self.clock += 1
        self.postordered_vertices.append(v)

def toposort(adj):
    dfs = DepthFirstSearch()
    dfs.run(adj)
    return reversed(dfs.postordered_vertices)

if __name__ == '__main__':
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

