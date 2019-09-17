#!/usr/bin/python3

# Contraction Hierarchies
# https://www.coursera.org/learn/algorithms-on-graphs/lecture/HV35U/highway-hierarchies-and-node-importance

import sys
import queue


# Maximum allowed edge length
maxlen = 2 * 10**6


def dijkstra(adj, cost, s, max_edges, ignore_v):
    n = len(adj)
    visited = [0] * n
    dist = [maxlen] * n
    dist[s] = 0
    edges_count = 0
    
    #q = [(dist[i], i) for i in range(n)]
    #heapq.heapify(q)
    q = queue.PriorityQueue()
    q.put((0, s))
    
    while not q.empty():
        #u = heapq.heappop(q)[1]
        u = q.get()[1]

        if visited[u] == 0:
            visited[u] = 1
            for v_i in range(len(adj[u])):                
                v = adj[u][v_i]
                if v != ignore_v:
                    if dist[v] > dist[u] + cost[u][v_i]:
                        dist[v] = dist[u] + cost[u][v_i]
                        #heapq.heappush(q, (dist[v], v))
                        q.put((dist[v], v))
                        edges_count += 1
                        if edges_count >= max_edges:
                            return dist
    return dist

class DistPreprocessSmall:
    def __init__(self, n, adj, cost):
        self.n = n
        self.INFINITY = n * maxlen
        self.adj = adj
        self.cost = cost
        self.clear()
        
        # Positions of nodes in the node ordering
        self.rank = [0] * n

        # Implement preprocessing here
        self.prepocess()
        

    def prepocess(self):
        q = queue.PriorityQueue()
        max_rank = 0

        contracted = [False] * self.n

        # Levels of nodes for node ordering heuristics
        level = [0] * self.n

        # At the end: new edges (augmentation), rank (and level) array is filled out.
        for v in range(self.n):
            q.put((0, v)) # TODO: is 0 OK as initial importance?

        while not q.empty():
            v = q.get()[1]

            if not contracted[v]:
                importance, level[v] = recompute_importance(v, level[v])
            
                if importance <= q.top(): # or strong "<" ?
                    self.conract(v)
                    self.rank[v] = max_rank
                    max_rank += 1
                    # self.rank[v] is a position in node order (returned by the preprocessing stage)
                    contracted[v] = True
                else:            
                    q.put((importance, v))


    def conract(self, v):
        # Witness Search https://www.coursera.org/learn/algorithms-on-graphs/lecture/WuGFB/witness-search
        # For each predecessor ui of v run Dij from ui ignoring v.
        # Stop Dij:
            # if d(ui, x) > max max [ l(u,v) + l(v,w) - l(w', w) ]    
            #    or k edges are processed (increase k from 1 to 5 ???)

        for u in self.adj[1][v]:
            dist = dijkstra(self.adj[0], self.cost[0], u, 5*len(self.adj[0][v]), v)
            for w in self.adj[0][v]:
                c = l(u, v) + l(v, w) # use self.cost[][][]
                if dist[w] > c:
                    self.add_shortcut(u, w, c)


    def add_shortcut(self, u, v, c):
        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)
    
    def recompute_importance(self, v, level):
        # https://www.coursera.org/learn/algorithms-on-graphs/lecture/Abyzw/node-ordering
        shortcut_count = 0
        neighbors = 0
        shortcut_cover = 0
        #level = 0
        # Compute correctly the values for the above heuristics before computing the node importance
        importance = (shortcut_count - len(self.adj[0][v]) - len(self.adj[1][v])) + neighbors + shortcut_cover + level
        return importance, level

    


    # ================================================================

    def clear(self):
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [False] * n
        self.workset = []

    # See description of this method in the starter for friend_suggestion
    def visit(side, v, dist):
        # Implement this method yourself
        pass

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        estimate = self.INFINITY
        visit(0, s, 0)
        visit(1, t, 0)
        # Implement the rest of the algorithm yourself

        # BiDij with specific stopping and moving according to rank[v] (using only upwards edges)

        return -1 if estimate == self.INFINITY else estimate


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)

    ch = DistPreprocessSmall(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s-1, t-1))