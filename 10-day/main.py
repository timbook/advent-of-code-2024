import numpy as np

file = 'input.txt'
raw = open(file, 'r').readlines()
mx = np.array([list(line.strip()) for line in raw]).astype(int)
R, C = mx.shape

class Node:
    def __init__(self, r, c):
        self.r, self.c = r, c
        self.value = mx[r, c]
        nbs = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
        self.nbs = [(r, c) for r, c in nbs if 0 <= r < R and 0 <= c < C]

    def __repr__(self):
        return f"Node({self.r}, {self.c}, {self.value})"

    def explore(self):
        if self.value == 9:
            return {(self.r, self.c)}

        peaks = set()
        for r, c in self.nbs:
            if mx[r, c] - self.value == 1:
                peaks |= nodes[(r, c)].explore()
        return peaks

    def explore_b(self):
        if self.value == 9:
            return 1

        peaks = 0
        for r, c in self.nbs:
            if mx[r, c] - self.value == 1:
                peaks += nodes[(r, c)].explore_b()
        return peaks

# Create nodes
nodes = {}
trailheads = []
for r in range(R):
    for c in range(C):
        n = Node(r, c)
        nodes[(r, c)] = n

        if n.value == 0:
            trailheads.append(n)

sol = sum([len(th.explore()) for th in trailheads])
print(f"A ::: {sol}")

sol = sum([th.explore_b() for th in trailheads])
print(f"B ::: {sol}")
