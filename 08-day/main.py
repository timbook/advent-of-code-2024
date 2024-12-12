from itertools import combinations
import numpy as np

file = 'input.txt'
raw = open(file, 'r').readlines()
mx = np.array([list(line.strip()) for line in raw])

xs, ys = np.where(mx != '.')
syms = {mx[x, y] for x, y in zip(xs, ys)}

antinodes = set()
for sym in syms:
    sym_locs = [np.array([r, c]) for r, c in zip(*list(np.where(mx == sym)))]
    for p, q in combinations(sym_locs, 2):
        d = p - q
        antinodes.add(tuple(p + d))
        antinodes.add(tuple(q - d))

R, C = mx.shape
antinodes_trim = set([n for n in antinodes if 0 <= n[0] < R and 0 <= n[1] < C])
sol = len(antinodes_trim)

print(f"A ::: {sol}")

def check_boundary(p, mx):
    r, c = tuple(p)
    return 0 <= r < R and 0 <= c < C

antinodes = set()
for sym in syms:
    sym_locs = [np.array([r, c]) for r, c in zip(*list(np.where(mx == sym)))]
    for p, q in combinations(sym_locs, 2):
        d = p - q

        inc = 0
        while True:
            p2 = p + inc*d
            
            if check_boundary(p2, mx):
                antinodes.add(tuple(p2))
                inc += 1
            else:
                break

        inc = 0
        while True:
            q2 = q - inc*d
            if check_boundary(q2, mx):
                antinodes.add(tuple(q2))
                inc += 1
            else:
                break

sol = len(antinodes)

print(f"B ::: {sol}")
