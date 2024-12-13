import numpy as np

#  file = 'sample-small.txt'
#  file = 'sample-large.txt'
file = 'input.txt'
raw = open(file, 'r').readlines()
mx = np.array([list(line.strip()) for line in raw])
R, C = mx.shape

class Node:
    def __init__(self, p):
        r, c = p
        self.p = p
        self.r, self.c = (r, c)
        self.sym = mx[r, c]

        nbs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        self.nbs = nbs
        self.nbs_trim = [(r, c) for r, c in nbs if 0 <= r < R and 0 <= c < C]

    def __repr__(self):
        return f"{self.sym}({self.r}, {self.c})"

    @property
    def perim(self):
        count = 0
        for r, c in self.nbs:
            if not (0 <= r < R):
                count += 1
            elif not (0 <= c < C):
                count += 1
            elif 0 <= r < R and 0 <= c < C and mx[r, c] != self.sym:
                count += 1
        return count

class Region:
    def __init__(self, p):
        node = Node(p)
        self.init_node = node
        self.sym = node.sym
        self.explore_nodes()

    def __repr__(self):
        return f"Region{self.sym}({self.init_node.p})"

    def explore_nodes(self):
        #  import pdb; pdb.set_trace()
        to_explore = [self.init_node]
        explored = []
        while to_explore:
            node = to_explore.pop()
            explored.append(node.p)

            for p in node.nbs:
                r, c = p
                if 0 <= r < R and 0 <= c < C and mx[r, c] == self.sym and p not in explored:
                    n = Node(p)
                    to_explore.append(n)

        self.nodes = [Node(p) for p in set(explored)]

    @property
    def area(self):
        return len(self.nodes)

    @property
    def perim(self):
        return sum(n.perim for n in self.nodes)


points = []
for r in range(R):
    for c in range(C):
        points.append((r, c))

regions = []
while points:
    p = points.pop()
    r = Region(p)
    for n in r.nodes:
        if n.p in points:
            points.remove(n.p)

    regions.append(r)
    
sol = sum(r.area*r.perim for r in regions)
print(f"A ::: {sol}")





