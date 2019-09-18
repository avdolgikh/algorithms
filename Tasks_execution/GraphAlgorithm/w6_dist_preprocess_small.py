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
    
    q = queue.PriorityQueue()
    q.put((0, s))
    
    while not q.empty():
        u = q.get()[1]

        if visited[u] == 0:
            visited[u] = 1
            for v_i in range(len(adj[u])):                
                v = adj[u][v_i]
                if v != ignore_v:
                    if dist[v] > dist[u] + cost[u][v_i]:
                        dist[v] = dist[u] + cost[u][v_i]                        
                        q.put((dist[v], v))
                        edges_count += 1
                        if edges_count >= max_edges:
                            return dist
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
        level = [0] * self.n

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
            
                if self.q.empty() or importance <= self.q.queue[0][0]: # or strong "<" ? # q.queue[0][0] means q.top()
                    self.conract(v)
                    self.rank[v] = self.max_rank
                    self.max_rank += 1
                    # self.rank[v] is a position in node order (returned by the preprocessing stage)
                    self.contracted[v] = True
                else:            
                    self.q.put((importance, v))

    def conract(self, v):
        # Witness Search https://www.coursera.org/learn/algorithms-on-graphs/lecture/WuGFB/witness-search
        # For each predecessor ui of v run Dij from ui ignoring v.
        # Stop Dij:
            # if d(ui, x) > max max [ l(u,v) + l(v,w) - l(w', w) ]    
            #    or k edges are processed (increase k from 1 to 5 ???)

        for u_i in range(len(self.adj[1][v])): # self.adj[1][v] are predecessors of v.
            u = self.adj[1][v][u_i]
            l_u_v = self.cost[1][v][u_i]
            dist = dijkstra(self.adj[0], self.cost[0], u, 5*len(self.adj[0][v]), v)
            for w_i in range(len(self.adj[0][v])): # self.adj[0][v] are successors of v.
                w = self.adj[0][v][w_i]
                l_v_w = self.cost[0][v][w_i]
                c = l_u_v + l_v_w
                if dist[w] > c:
                    self.add_shortcut(u, w, c)

        for neighbor in self.adj[1][v] + self.adj[0][v]:
            self.level[neighbor] = max( self.level[neighbor], self.level[v] + 1 )

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

    def recompute_importance(self, v):
        # https://www.coursera.org/learn/algorithms-on-graphs/lecture/Abyzw/node-ordering

        # EACH of the 4 quantities is necessary!!!

        # !!! TODO:
        shortcut_count = 0
        # shortcut_count - number of added shortcuts s(v); how many shorcuts would be added if we contract this node v.
        #edge_difference = shortcut_count - len(self.adj[0][v]) - len(self.adj[1][v])        
        edge_difference = 0
        
        n_contracted_neighbors = 0 # number of contracted neighbors
        shortcut_cover = 0 # number of neighbors that we HAVE TO short cut...

        for neighbor in self.adj[1][v] + self.adj[0][v]:
            if self.contracted[neighbor]:
                n_contracted_neighbors += 1
            if len(self.adj[1][neighbor] + self.adj[0][neighbor]) == 1:
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

        # Implement preprocessing here
        self.prepocess()
        
    # ================================================================

    def prepocess(self):
        q = queue.PriorityQueue()
        max_rank = 0

        contracted = [False] * self.n

        # Levels of nodes for node ordering heuristics
        level = [0] * self.n

        # NODE ORDERING:
        # https://www.coursera.org/learn/algorithms-on-graphs/lecture/Abyzw/node-ordering

        # At the end: new edges (augmentation), rank (and level) array is filled out.
        for v in range(self.n):
            q.put((-self.INFINITY, v))

        while not q.empty():
            v = q.get()[1]

            if not contracted[v]:
                importance = self.recompute_importance(v, level[v], contracted)
            
                if q.empty() or importance <= q.queue[0][0]: # or strong "<" ? # q.queue[0][0] means q.top()
                    self.conract(v, level)
                    self.rank[v] = max_rank
                    max_rank += 1
                    # self.rank[v] is a position in node order (returned by the preprocessing stage)
                    contracted[v] = True
                else:            
                    q.put((importance, v))

    def conract(self, v, level):
        # Witness Search https://www.coursera.org/learn/algorithms-on-graphs/lecture/WuGFB/witness-search
        # For each predecessor ui of v run Dij from ui ignoring v.
        # Stop Dij:
            # if d(ui, x) > max max [ l(u,v) + l(v,w) - l(w', w) ]    
            #    or k edges are processed (increase k from 1 to 5 ???)

        for u_i in range(len(self.adj[1][v])): # self.adj[1][v] are predecessors of v.
            u = self.adj[1][v][u_i]
            l_u_v = self.cost[1][v][u_i]
            dist = dijkstra(self.adj[0], self.cost[0], u, 5*len(self.adj[0][v]), v)
            for w_i in range(len(self.adj[0][v])): # self.adj[0][v] are successors of v.
                w = self.adj[0][v][w_i]
                l_v_w = self.cost[0][v][w_i]
                c = l_u_v + l_v_w
                if dist[w] > c:
                    self.add_shortcut(u, w, c)

        for neighbor in self.adj[1][v] + self.adj[0][v]:
            level[neighbor] = max( level[neighbor], level[v] + 1 )

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

    def recompute_importance(self, v, level, contracted):
        # https://www.coursera.org/learn/algorithms-on-graphs/lecture/Abyzw/node-ordering

        # EACH of the 4 quantities is necessary!!!

        # !!! TODO:
        shortcut_count = 0
        # shortcut_count - number of added shortcuts s(v); how many shorcuts would be added if we contract this node v.
        #edge_difference = shortcut_count - len(self.adj[0][v]) - len(self.adj[1][v])        
        edge_difference = 0
        
        n_contracted_neighbors = 0 # number of contracted neighbors
        shortcut_cover = 0 # number of neighbors that we HAVE TO short cut...

        for neighbor in self.adj[1][v] + self.adj[0][v]:
            if contracted[neighbor]:
                n_contracted_neighbors += 1
            if len(self.adj[1][neighbor] + self.adj[0][neighbor]) == 1:
                shortcut_cover += 1
        
        importance = edge_difference + n_contracted_neighbors + shortcut_cover + level # add weights

        return importance


    # ================================================================

    def clear(self):
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [False] * n
        self.workset = []

    def relax(self, q, side, v, dist):
        if self.bidistance[side][v] > dist:
            self.bidistance[side][v] = dist
            q[side].put((dist, v))

    def calc_dist(self):
        distance = self.INFINITY
        for u in self.workset:
            if self.bidistance[0][u] + self.bidistance[1][u] < distance:
                distance = self.bidistance[0][u] + self.bidistance[1][u]
        
        return -1 if distance == self.INFINITY else distance

    def process_min(self, q, side):
        finished = True
        distance = -1

        if not q[side].empty():
            v = q[side].get()[1]

            if not self.visited[v]:
                finished = False
                self.visited[v] = True
                self.workset.append(v)
                for u_i in range(len(self.adj[side][v])):
                    u = self.adj[side][v][u_i]
                    self.relax(q, side, u, self.bidistance[side][v] + self.cost[side][v][u_i])

        if finished:
            distance = self.calc_dist()

        return finished, distance


    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        estimate = self.INFINITY
        self.relax(q, 0, s, 0)
        self.relax(q, 1, t, 0)

        # BiDij with specific stopping and moving according to rank[v] (using only upwards edges)

        while True:
            for side in [0, 1]:
                finished, distance = self.process_min(q, side)
                if finished:
                    return distance

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

    ch = ContractionHierarchies(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s-1, t-1))