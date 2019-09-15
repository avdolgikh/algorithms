#Uses python3

import sys

def explore(adj, v, visited, ccNum, cc):
    visited[v] = 1
    ccNum[v] = cc
    for u in adj[v]:
        if visited[u] == 0:
            explore(adj, u, visited, ccNum, cc)

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

    visited = [0] * n
    cc = 0
    ccNum = [0] * n

    for v in range(n):
        if visited[v] == 0:
            cc += 1
            explore(adj, v, visited, ccNum, cc)

    print(cc)
