#Uses python3

import sys
import numpy as np

def BelmanFord(adjacency_matrix, cost, origin_vertex, big_distance):
    n = len(adjacency_matrix)
    dist = [big_distance] * n
    prev = [-1] * n
    dist[origin_vertex] = 0
    shortest = [1] * n

    for i in range(2*n):
        for v in range(n):
            for u_i in range(len(adjacency_matrix[v])):
                u = adjacency_matrix[v][u_i]
                if dist[u] > dist[v] + cost[v][u_i]:
                    dist[u] = dist[v] + cost[v][u_i]
                    prev[u] = v
                    if i > n-2:
                        shortest[u] = 0
    return dist, shortest

def shortet_paths(adj, cost, s):
    big_distance = np.inf
    return BelmanFord(adj, cost, s, big_distance)
    


if __name__ == '__main__':
    input = sys.stdin.read()

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

    s = data[0]
    s -= 1

    dist, shortest = shortet_paths(adj, cost, s)

    for x in range(n):
        if shortest[x] == 0:
            print('-')
        elif dist[x] == np.inf:
            print('*')
        else:
            print(dist[x])
        
