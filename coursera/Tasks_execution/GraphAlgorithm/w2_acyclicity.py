#Uses python3

import sys

def explore_cycle(adj, v, visited, pre, post):
    visited[v] = 1
    #previsit(v, pre)
    for u in adj[v]:
        if visited[u] == 0:
            if explore_cycle(adj, u, visited, pre, post):
                return True
        elif post[u] == 0:
            return True
    postvisit(v, post)
    return False

def previsit(v, pre):
    global clock
    pre[v] = clock
    clock += 1
    
def postvisit(v, post):
    global clock
    post[v] = clock
    clock += 1

def acyclic(n, adj):
    visited = [0] * n
    pre = [0] * n
    post = [0] * n

    for v in range(n):
        if visited[v] == 0:
            if explore_cycle(adj, v, visited, pre, post):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    clock = 1

    print(acyclic(n, adj))
    

    
