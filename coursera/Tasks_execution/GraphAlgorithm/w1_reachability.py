#Uses python3

import sys

def explore(adj, v, visited, pre, post):
    visited[v] = 1
    previsit(v, pre)
    for u in adj[v]:
        if visited[u] == 0:
            explore(adj, u, visited, pre, post)
    postvisit(v, post)

def previsit(v, pre):
    global clock
    pre[v] = clock
    clock += 1
    
def postvisit(v, post):
    global clock
    post[v] = clock
    clock += 1

def reach(pre, post, x, y):
    if pre[x] < pre[y]:
        return int(post[x] > pre[y])
    else:
        return int(post[y] > pre[x])

if __name__ == '__main__':
    #input = "4 4 1 2 3 2 4 3 1 4 1 4"
    #input = "4 2 1 2 3 2 1 4"
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    clock = 1

    visited = [0] * n
    pre = [0] * n
    post = [0] * n

    for v in range(n):
        if visited[v] == 0:
            explore(adj, v, visited, pre, post)

    print(reach(pre, post, x, y))
