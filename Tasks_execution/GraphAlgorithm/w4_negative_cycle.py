#Uses python3

import sys
import numpy as np

def BelmanFord(adjacency_matrix, cost, origin_vertex, big_distance):
    n = len(adjacency_matrix)
    dist = [big_distance] * n
    prev = [-1] * n
    dist[origin_vertex] = 0
    updated = False

    for _ in range(n):
        updated = False
        for v in range(n):
            for u_i in range(len(adjacency_matrix[v])):
                u = adjacency_matrix[v][u_i]
                if dist[u] > dist[v] + cost[v][u_i]:
                    dist[u] = dist[v] + cost[v][u_i]
                    prev[u] = v
                    updated = True
    return updated

def negative_cycle(adj, cost):
    big_distance = np.inf
    n = len(adj)
    for v in range(n):
        if BelmanFord(adj, cost, v, big_distance):
            return 1
    return 0


if __name__ == '__main__':
    #input = sys.stdin.read()
    #input = "4 4 1 2 -5 4 1 2 2 3 2 3 1 1" # with negative cycles
    input = "4 4 1 2 5 4 1 2 2 3 2 3 1 1" # with positive cycles
    #input = "4 4 1 2 -5 4 1 2 3 1 1" # uncycled

    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]

    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    print(negative_cycle(adj, cost))
