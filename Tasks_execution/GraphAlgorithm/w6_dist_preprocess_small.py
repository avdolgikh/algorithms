#!/usr/bin/python3

# Contraction Hierarchies
# https://www.coursera.org/learn/algorithms-on-graphs/lecture/HV35U/highway-hierarchies-and-node-importance

import sys
import queue


# Maximum allowed edge length
maxlen = 2 * 10**6


def dijkstra(adj, cost, s, max_edges, ignore_v, dist_limit):
    n = len(adj)
    visited = [False] * n
    dist = [maxlen] * n
    dist[s] = 0
    edges_count = 0
    
    q = queue.PriorityQueue()
    q.put((0, s))
    
    while not q.empty():
        u = q.get()[1]

        if dist[u] > dist_limit:
            return dist

        if not visited[u]:
            visited[u] = True

            edges_count += 1
            if edges_count >= max_edges:
                return dist

            for v_i in range(len(adj[u])):
                v = adj[u][v_i]
                if v != ignore_v:
                    if dist[v] > dist[u] + cost[u][v_i]:
                        dist[v] = dist[u] + cost[u][v_i]
                        q.put((dist[v], v))
                        
    return dist


class ContractionHierarchiesPreprocessor:
    def __init__(self, n, adj, cost, rank):
        self.n = n
        self.INFINITY = n * maxlen
        self.adj = adj
        self.cost = cost
        self.rank = rank
        self.q = queue.PriorityQueue()
        self.max_rank = 0
        self.contracted = [False] * self.n
        # Levels of nodes for node ordering heuristics
        self.level = [0] * self.n

    def prepocess(self):
        # NODE ORDERING:
        # https://www.coursera.org/learn/algorithms-on-graphs/lecture/Abyzw/node-ordering

        # At the end: new edges (augmentation), rank (and level) array is filled out.
        for v in range(self.n):
            self.q.put((-self.INFINITY, v))

        while not self.q.empty():
            v = self.q.get()[1]

            if not self.contracted[v]:
                importance = self.recompute_importance(v)
            
                if self.q.empty() or importance <= self.q.queue[0][0]: # or strong "<" ? # q.queue[0][0] means q.head()
                    self.conract(v)

                    # self.rank[v] is a position in node order (returned by the preprocessing stage)
                    self.rank[v] = self.max_rank

                    self.max_rank += 1                    
                    self.contracted[v] = True

                else:            
                    self.q.put((importance, v))

        #self.remove_going_down_edges() # TODO: make this deletion during contracting stage!

    def remove_going_down_edges(self):
        # go through WHOLE graph and delete (u, v) if self.rank[u] > self.rank[v]

        def remove_going_down_edges(side):
            for u in range(self.n):
                adj = []
                cost = []
                for v_i in range(len(self.adj[side][u])):
                    v = self.adj[side][u][v_i]
                    if self.rank[u] <= self.rank[v]:
                        adj.append(self.adj[side][u][v_i])
                        cost.append(self.cost[side][u][v_i])
                self.adj[side][u] = adj
                self.cost[side][u] = cost

        for side in [0, 1]:
            remove_going_down_edges(side)

    def conract(self, v):
        self.witness_search(v)

        for neighbor in (self.adj[1][v] + self.adj[0][v]):
            self.level[neighbor] = max( self.level[neighbor], self.level[v] + 1 )

    def witness_search(self, v, add_shortcuts=True):
        # Witness Paths https://www.coursera.org/learn/algorithms-on-graphs/lecture/AWFGa/preprocessing, 4:44
        # Witness Search https://www.coursera.org/learn/algorithms-on-graphs/lecture/WuGFB/witness-search
        # For each predecessor ui of v run Dij from ui ignoring v.
        # Stop Dij:
            # if d(ui, x) > max max [ l(u,v) + l(v,w) - l(w', w) ]    
            #    or k edges are processed (increase k from 1 to 5 ???)

        #max_successor_dist = max(self.cost[0][v])
        dist_limit = ( max(self.cost[1][v]) if len(self.cost[1][v]) > 0 else 0 ) + ( max(self.cost[0][v]) if len(self.cost[0][v]) > 0 else 0 )

        shortcut_count = 0

        for u_i in range(len(self.adj[1][v])): # self.adj[1][v] are predecessors of v.
            u = self.adj[1][v][u_i]
            l_u_v = self.cost[1][v][u_i]

            #dist_limit = l_u_v + max_successor_dist

            dist = dijkstra(self.adj[0], self.cost[0], u, 100, v, dist_limit)

            for w_i in range(len(self.adj[0][v])): # self.adj[0][v] are successors of v.
                w = self.adj[0][v][w_i]
                l_v_w = self.cost[0][v][w_i]
                c = l_u_v + l_v_w
                if dist[w] > c:
                    shortcut_count += 1
                    if add_shortcuts:
                        self.add_shortcut(u, w, c)
                        
        return shortcut_count

    def add_shortcut(self, u, v, c):

        #if self.contracted[v]:
        #    return

        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)

    def recompute_importance(self, v):
        # https://www.coursera.org/learn/algorithms-on-graphs/lecture/Abyzw/node-ordering

        # EACH of the 4 quantities is necessary!!!
        
        shortcut_count = self.witness_search(v, add_shortcuts = False)
        # heuristic: shortcut_count = len(self.adj[0][v]) * len(self.adj[1][v])
        # shortcut_count - number of added shortcuts s(v); how many shortcuts would be added if we contract this node v.
        edge_difference = shortcut_count - len(self.adj[0][v]) - len(self.adj[1][v])
        #edge_difference = 0
        
        n_contracted_neighbors = 0 # number of contracted neighbors
        shortcut_cover = 0 # number of neighbors that we HAVE TO short cut...

        for neighbor in (self.adj[1][v] + self.adj[0][v]):
            if self.contracted[neighbor]:
                n_contracted_neighbors += 1
            if len(self.adj[1][neighbor] + self.adj[0][neighbor]) == 1: # ! or < 3 !? it can be 2: one in, one out; so it is important...
                shortcut_cover += 1
        
        importance = edge_difference + n_contracted_neighbors + shortcut_cover + self.level[v] # add weights

        return importance



class ContractionHierarchies:
    def __init__(self, n, adj, cost):
        self.n = n
        self.INFINITY = n * maxlen
        self.adj = adj
        self.cost = cost
        self.clear()
        
        # Positions of nodes in the node ordering
        self.rank = [0] * n

        preprocessor = ContractionHierarchiesPreprocessor(n, self.adj, self.cost, self.rank)
        preprocessor.prepocess()
        
    
    def clear(self):
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [[False] * n, [False] * n]
        self.estimate = self.INFINITY

    def relax(self, q, side, v, dist):
        if self.bidistance[side][v] > dist:
            self.bidistance[side][v] = dist
            q[side].put((dist, v))

    def process_one_side_search(self, q, side):

        if not q[side].empty():
            v = q[side].get()[1]

            if not self.visited[side][v]:
                self.visited[side][v] = True

                if self.bidistance[side][v] <= self.estimate:
                    for u_i in range(len(self.adj[side][v])):
                        u = self.adj[side][v][u_i]
                        #if self.rank[u] > self.rank[v]:
                        self.relax(q, side, u, self.bidistance[side][v] + self.cost[side][v][u_i])

                inverted_side = int(not bool(side))
                if self.visited[inverted_side][v] and (self.bidistance[0][v] + self.bidistance[1][v]) < self.estimate:
                    self.estimate = self.bidistance[0][v] + self.bidistance[1][v]

    def query(self, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.relax(q, 0, s, 0)
        self.relax(q, 1, t, 0)

        while not q[0].empty() or not q[1].empty():
            for side in [0, 1]:
                self.process_one_side_search(q, side)

        return -1 if self.estimate == self.INFINITY else self.estimate


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

    ch = ContractionHierarchies(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s-1, t-1))


"""
Failed case #3/6: (Wrong answer)

Preprocess input:
10 20
7 4 923
1 2 115
2 7 938
10 4 615
5 6 951
6 4 24
9 7 95
3 5 337
5 9 252
6 8 466
6 2 234
9 3 670
5 3 156
8 4 875
3 1 926
10 2 210
10 9 535
7 10 429
2 3 688
2 10 444

Input:
10
7 8
5 2
8 10
3 1
5 7
4 10
5 3
3 1
9 4
3 9

Your output:
3081
1185
-1
926
347
-1
156
926
1018
589

Correct output:
3081
!!! 986
-1
926
347
-1
156
926
1018
589

------
3081
986
-1
926
347
-1
156
926
1018
589
----
3081
986
-1
926
347
-1
156
926
1018
589

 (Time used: 0.00/10.00, preprocess time used: 0.02/50.0, memory used: 0/2147483648.)
"""


"""
Failed case #4/6: Wrong answer

 (Time used: 0.43/10.00, preprocess time used: 6.29/50.0, memory used: 0/2147483648.)

"""