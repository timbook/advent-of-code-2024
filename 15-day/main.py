import numpy as np

#  file = 'sample-tiny.txt'
#  file = 'sample.txt'
file = 'input.txt'
raw = open(file, 'r').read()

raw_grid, raw_moves = raw.split('\n\n')

mx = np.array([list(line) for line in raw_grid.split('\n')])
moves = raw_moves.replace('\n', '')

def instr_map(move, r, c):
    return {
        '>': (r, c + 1),
        '<': (r, c - 1),
        '^': (r - 1, c),
        'v': (r + 1, c)
    }[move]

class Grid:
    def __init__(self, mx):
        self.mx = mx

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.mx])

    @property
    def fish_loc(self):
        xs, ys = np.where(self.mx == '@')
        return xs[0], ys[0]

    @property
    def score(self):
        R, C = self.mx.shape

        total = 0
        for r in range(R):
            for c in range(C):
                if self.mx[r, c] == 'O':
                    total += 100*r + c

        return total

    def move_set(self, instrs):
        for i in instrs:
            self.move(i)

    def is_push_to_wall(self, r, c, instr):
        new_r, new_c = instr_map(instr, r, c)
        if self.mx[new_r, new_c] == '#':
            return True
        elif self.mx[new_r, new_c] == '.':
            return False
        else:
            return self.is_push_to_wall(new_r, new_c, instr)

    def move(self, instr):
        r, c = self.fish_loc
        new_r, new_c = instr_map(instr, r, c)

        if self.mx[new_r, new_c] == '#':
            return

        if self.is_push_to_wall(r, c, instr):
            return

        popped_sym = self.mx[new_r, new_c]

        self.mx[r, c] = '.'
        self.mx[new_r, new_c] = '@'
        self.move_next(popped_sym, new_r, new_c, instr)

    def move_next(self, sym, r, c, instr):
        if sym == '.':
            return

        new_r, new_c = instr_map(instr, r, c)

        if self.mx[new_r, new_c] == '#':
            return

        popped_sym = self.mx[new_r, new_c]
        self.mx[new_r, new_c] = sym
        self.move_next(popped_sym, new_r, new_c, instr)

g = Grid(mx)

for move in moves:
    g.move(move)

sol = g.score
print(f"A ::: {sol}")
