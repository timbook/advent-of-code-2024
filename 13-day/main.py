import re
import numpy as np

file = 'input.txt'
raw = open(file, 'r').read()

pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
raw_parsed = re.findall(pattern, raw)

class System:
    def __init__(self, line, const=0):
        line = [int(i) for i in line]
        self.A = np.array([
            [line[0], line[2]],
            [line[1], line[3]]
        ])
        self.b = np.array([line[4], line[5]]) + const
        self.solve()

    def solve(self):
        self.sol = np.linalg.solve(self.A, self.b)

    def cost(self):
        return 3*self.sol[0] + self.sol[1]

    def is_int(self):
        c = self.cost()
        return np.all(np.abs(self.sol - np.round(self.sol)) < 1e-4)

systems = [System(item) for item in raw_parsed]
costs = [s.cost() for s in systems if s.is_int()]
sol = round(np.sum(costs))

print(f"A ::: {sol}")

C = 10_000_000_000_000
systems = [System(item, const=C) for item in raw_parsed]
costs = [s.cost() for s in systems if s.is_int()]
sol = round(np.sum(costs))
print(f"B ::: {sol}")
