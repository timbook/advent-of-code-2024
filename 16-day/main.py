import numpy as np
import networkx as nx

file = 'sample1.txt'
#  file = 'sample2.txt'
#  file = 'input.txt'
raw = open(file, 'r').read().strip()
mx = np.array([list(row.strip()) for row in raw.split('\n')])
R, C = mx.shape

def get_nbs(node):
    r, c = node
    nbs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    return [(r, c) for r, c in nbs if 0 <= r < R and 0 <= c < C]

def get_coord_by_sym(mx, sym):
    xs, ys = np.where(mx == sym)
    return xs[0], ys[0]

def shortest_path(G, start, end):
    pass
    

G = nx.Graph()

# Add nodes
for r in range(R):
    for c in range(C):
        if mx[r, c] in'.SE':
            G.add_node((r, c))

# Add edges
for node in G.nodes:
    nbs = get_nbs(node)
    for nb in nbs:
        if nb in G.nodes:
            G.add_edge(node, nb)


start = get_coord_by_sym(mx, 'S')
end = get_coord_by_sym(mx, 'E')

sol_path = shorted_path(G, start, end)
#  scores = [score_path(p) for p in paths]
#  sol = min(scores)
#  print(f"A ::: {sol}")
