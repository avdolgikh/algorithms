#Uses python3

import sys
#import queue
import heapq

def dijkstra(adjacency_matrix, cost, origin_vertex, big_distance):
    n = len(adjacency_matrix)
    visited = [0] * n
    dist = [big_distance] * n
    prev = [-1] * n
    dist[origin_vertex] = 0
    heap = [(dist[i], i) for i in range(n)]
    heapq.heapify(heap)
    while len(heap) > 0:
        u = heapq.heappop(heap)[1]
        if visited[u] == 0:
            visited[u] = 1
            for v_i in range(len(adjacency_matrix[u])):
                v = adjacency_matrix[u][v_i]
                if dist[v] > dist[u] + cost[u][v_i]:
                    dist[v] = dist[u] + cost[u][v_i]
                    prev[v] = u
                    heapq.heappush(heap, (dist[v], v))
    return dist
            
    
 
def distance(adj, cost, s, t):
    big_distance = sum(sum(cost, []))
    dist = dijkstra(adj, cost, s, big_distance)
    if dist[t] == big_distance:
        return -1
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1

    print(distance(adj, cost, s, t))
