#Uses python3

import sys

sys.setrecursionlimit(200000)

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


def number_of_strongly_connected_components(adj, reversed_graph_adj):
    scc_count = 0

    dfs = DepthFirstSearch()
    dfs.run(reversed_graph_adj)

    visited = [0] * len(reversed_graph_adj)

    def explore(v):
        visited[v] = 1
        for u in adj[v]:
            if visited[u] == 0:
                explore(u)

    for v in reversed(dfs.postordered_vertices):
        if visited[v] == 0:
            explore(v)
            scc_count += 1

    return scc_count

if __name__ == '__main__':
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    reversed_edges = list(zip(data[1:(2 * m):2], data[0:(2 * m):2])) # reversed !

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    reversed_graph_adj = [[] for _ in range(n)]
    for (a, b) in reversed_edges:
        reversed_graph_adj[a - 1].append(b - 1)

    print(number_of_strongly_connected_components(adj, reversed_graph_adj))
