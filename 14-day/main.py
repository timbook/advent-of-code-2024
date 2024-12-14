import re
import numpy as np
import matplotlib.pyplot as plt

#  file = 'sample.txt'
file = 'input.txt'
raw = open(file, 'r').read()
pattern = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'
data = re.findall(pattern, raw)

#  H, W = 7, 11
H, W = 103, 101

class Robot:
    def __init__(self, tup):
        px, py, vx, vy = tup
        self.px = int(px)
        self.py = int(py)
        self.vx = int(vx)
        self.vy = int(vy)

    def __repr__(self):
        return f'Robot(p=({self.px}, {self.py}), v=({self.vx}, {self.vy}))'

    def move_n(self, n):
        self.px = (self.px + n*self.vx) % W
        self.py = (self.py + n*self.vy) % H

robots = [Robot(d) for d in data]
for r in robots:
    r.move_n(100)

h_mid = H // 2
w_mid = W // 2

# Quadrant checks
Q1 = sum(1 for r in robots if r.px > w_mid and r.py < h_mid)
Q2 = sum(1 for r in robots if r.px < w_mid and r.py < h_mid)
Q3 = sum(1 for r in robots if r.px < w_mid and r.py > h_mid)
Q4 = sum(1 for r in robots if r.px > w_mid and r.py > h_mid)

# Not 88046400
sol = Q1*Q2*Q3*Q4
print(f"A ::: {sol}")

robots = [Robot(d) for d in data]

#  7055 works
track = []
for i in range(10000):
    grid = np.zeros((H, W), dtype=int)
    for r in robots:
        r.move_n(1)
        c, r = r.px, r.py
        grid[r, c] += 1

    n_mid = np.sum(grid == 1)
    track.append(n_mid)

#  plt.plot(track)
#  plt.show()

robots = [Robot(d) for d in data]
for r in robots:
    r.move_n(7055)

for r in robots:
    c, r = r.px, r.py
    grid[r, c] += 1

plt.imshow(grid)
plt.savefig('tree.png')

print(f'B ::: 7055')
