from collections import defaultdict
class Graph(object):
    def __init__(self, n):
        # self.nodes = list(range(n))
        self.adjacent = defaultdict(list)
        self.distance = [-1] * n
    def connect(self, x, y):
        self.adjacent[x].append(y)
        self.adjacent[y].append(x)
    def find_all_distance(self, s):
        # self.nodes[s] is the head
        queue = []
        # enqueue and flag
        # here the distance to be calculated can be used as flag
        queue.append(s)
        self.distance[s] = 0
        while queue:
            top = queue.pop(0)
            for adj in self.adjacent[top]:
                if self.distance[adj] < 0:
                    queue.append(adj)
                    self.distance[adj] = self.distance[top] + 6

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distance(s-1)
    distance = graph.distance
    del(distance[s-1])
    print(' '.join(str(dist) for dist in distance))
