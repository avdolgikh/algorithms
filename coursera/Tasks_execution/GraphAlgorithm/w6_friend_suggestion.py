#!/usr/bin/python3

import sys
import queue


"""
Case #2/7:

Input:
5 20
1 2 667
1 3 677
1 4 700
1 5 622
2 1 118
2 3 325
2 4 784
2 5 11
3 1 585
3 2 956
3 4 551
3 5 559
4 1 503
4 2 722
4 3 331
4 5 366
5 1 880
5 2 883
5 3 461
5 4 228
10
1 1
1 2
1 3
1 4
1 5
2 1
2 2
2 3
2 4
2 5

Correct output:
0
667
677
700
622
118
0
325
239
11
"""

class BiDij:
    def __init__(self, n):
        self.n = n;                             # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.clear()

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                       # All the nodes visited by forward or backward search

    def relax(self, q, side, v, dist):
        """Try to relax the distance to node v from direction side by value dist."""
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            q[side].put((dist, v))

    def calc_dist(self):
        distance = self.inf
        for u in self.workset:
            if self.d[0][u] + self.d[1][u] < distance:
                distance = self.d[0][u] + self.d[1][u]
        if distance == self.inf:
            distance = -1
        return distance

    def process_min(self, q, side, adj, cost):
        finished = True
        distance = -1

        if not q[side].empty():
            v = q[side].get()[1]

            if not self.visited[v]:
                finished = False
                self.visited[v] = True
                self.workset.append(v)
                for u_i in range(len(adj[side][v])):
                    u = adj[side][v][u_i]
                    self.relax(q, side, u, self.d[side][v] + cost[side][v][u_i])

        if finished:
            distance = self.calc_dist()

        return finished, distance

    def query(self, adj, cost, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.relax(q, 0, s, 0)
        self.relax(q, 1, t, 0)

        while True:
            for side in [0, 1]:
                finished, distance = self.process_min(q, side, adj, cost)
                if finished:
                    return distance

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]

    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)

    t, = readl()

    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
