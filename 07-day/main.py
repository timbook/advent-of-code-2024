from itertools import permutations
from collections import deque

file = 'sample.txt'
raw = open(file, 'r').readlines()

add = lambda a, b: a + b
mul = lambda a, b: a * b

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
        import pdb; pdb.set_trace()
        for op_list in permutations([add, mul], n_ops):
            ans = self.nums[0]
            import pdb; pdb.set_trace()
            for op, b in zip(op_list, self.nums[1:]):
                print(f"Op({ans}, {b}) -> {op(ans, b)}")
                ans = op(ans, b)

            if ans == self.res:
                count += 1
        return count
            
            

eqns = [Equation(line) for line in raw]
#  sols = [eqn.res for eqn in eqns if eqn.count_ops() > 0]
#  sol = sum(sols)
#  print(f"A ::: {sol}")
