import re

#  file = 'sample.txt'
file = 'input.txt'
raw = open(file, 'r').readlines()

patterns = [f"^{p}" for p in raw[0].strip().split(', ')]
towels = [line.strip() for line in raw[2:]]

class Node:
    def __init__(self, towel):

        self.towel = towel
        self.children = []
        self.done = False if self.towel else True

    def __repr__(self):
        return f"Node({self.towel})"

    def explore(self, patterns):
        for pattern in patterns:
            if re.match(pattern, self.towel):
                remaining = re.sub(pattern, '', self.towel)
                new_node = Node(remaining)
                new_node.explore(patterns)
                self.children.append(new_node)

        #  for child in self.children:
            #  child.explore(patterns)

    def check(self):
        return self.done or any([c.check() for c in self.children])

trees = [Node(t) for t in towels]

print("Exploring...")
for i, t in enumerate(trees):
    print(f"Tree #{i + 1}")
    t.explore(patterns)

print("Checking...")
possible = [t.check() for t in trees]
sol = sum(possible)
print(f"A ::: {sol}")
