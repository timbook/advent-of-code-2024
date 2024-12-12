from itertools import product
from collections import deque

#  file = 'sample.txt'
file = 'input.txt'
raw = open(file, 'r').readlines()

add = lambda a, b: a + b
mul = lambda a, b: a * b
cat = lambda a, b: int(str(a) + str(b))

class Equation:
    def __init__(self, line):
        lhs, rhs = line.strip().split(': ')
        self.nums = [int(n) for n in rhs.split()]
        self.res = int(lhs)

    def __repr__(self):
        return f"{self.res} = {self.nums}"

    def count_ops(self):
        n_ops = len(self.nums) - 1
        count = 0
        for ops in product(*['*+' for _ in range(n_ops)]):
            ops = deque(ops)
            vec = deque(self.nums.copy())
            while ops:
                #  print(f"vec = {vec}")
                op = {'*': mul, '+': add}[ops.popleft()]
                a = vec.popleft()
                b = vec.popleft()
                vec.appendleft(op(a, b))

            if vec[0] == self.res:
                count += 1

        return count

    def count_ops_b(self):
        n_ops = len(self.nums) - 1
        count = 0
        for ops in product(*['*+|' for _ in range(n_ops)]):
            ops = deque(ops)
            vec = deque(self.nums.copy())
            while ops:
                #  print(f"vec = {vec}")
                op = {'*': mul, '+': add, '|': cat}[ops.popleft()]
                a = vec.popleft()
                b = vec.popleft()
                vec.appendleft(op(a, b))

            if vec[0] == self.res:
                count += 1

        return count

            

eqns = [Equation(line) for line in raw]
sols = [eqn.res for eqn in eqns if eqn.count_ops() > 0]
sol = sum(sols)
print(f"A ::: {sol}")

eqns = [Equation(line) for line in raw]
sols = [eqn.res for eqn in eqns if eqn.count_ops_b() > 0]
sol = sum(sols)
print(f"B ::: {sol}")
