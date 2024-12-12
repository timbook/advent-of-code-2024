import numpy as np

file = 'input.txt'
raw = open(file, 'r').readlines()
mx = np.array([list(line.strip()) for line in raw])

class Grid:
    def __init__(self, mx):
        self.mx = mx
        self.hist = set()

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.mx])

    def plot_hist(self):
        hmx = np.zeros_like(self.mx, dtype=str)
        hmx[:, :] = '.'
        for r, c in self.hist:
            hmx[r, c] = 'X'
        for row in hmx:
            print(''.join(row))

    def pos(self):
        xs, ys = np.where(
            (self.mx == 'v') | \
            (self.mx == '^') | \
            (self.mx == '>') | \
            (self.mx == '<')
        )
        r, c = xs[0], ys[0]
        self.hist.add((r, c))
        return r, c

    def rotate(self, sym, old_r, old_c, new_r, new_c):
        next_square = self.mx[new_r, new_c]
        if next_square == '#':
            new_sym = {'>': 'v', 'v': '<', '<': '^', '^': '>'}[sym]    
            self.mx[old_r, old_c] = new_sym
            return True
        return False

    def move(self):
        R, C = self.mx.shape
        r, c = self.pos()
        sym = self.mx[r, c]
        if sym == 'v':
            new_r, new_c = r + 1, c
        elif sym == '^':
            new_r, new_c = r - 1, c
        elif sym == '<':
            new_r, new_c = r, c - 1
        elif sym == '>':
            new_r, new_c = r, c + 1

        if new_r < 0 or new_c < 0 or new_c >= C or new_r >= R:
            self.mx[r, c] = '.'
            return False

        # Rotate if needed
        if self.rotate(sym, r, c, new_r, new_c):
            return True

        next_square = self.mx[new_r, new_c]
        self.mx[r, c] = '.'
        self.mx[new_r, new_c] = sym
        return True

g = Grid(mx.copy())
while g.move():
    pass

sol = len(g.hist)
print(f"A ::: {sol}")

# Get origin
xs, ys = np.where(
    (mx == 'v') | \
    (mx == '^') | \
    (mx == '>') | \
    (mx == '<')
)
origin = xs[0], ys[0]

R, C = mx.shape
tot = R*C
loop_points = set()

for i, (r, c) in enumerate(g.hist - {origin}):
    if i % 100 == 0:
        print(f"Iteration: {i + 1}")
    mx_new = mx.copy()
    mx_new[r, c] = '#'
    g_new = Grid(mx_new)
    count = 0
    while g_new.move():
        count += 1
        if tot < count:
            loop_points.add((r, c))
            break

print(f"B ::: {len(loop_points)}")
