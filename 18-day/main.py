import numpy as np
import networkx as nx

#  file = 'sample.txt'
file = 'input.txt'
raw = open(file, 'r').readlines()

S = 7 if file == 'sample.txt' else 71
kb = 12 if file == 'sample.txt' else 1024

def get_nbs(r, c, S):
    candidates = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    return [
        (r, c) for r, c in candidates if 0 <= r < S and 0 <= c < S
    ]

# Construct mx
mx = np.zeros((S, S), dtype=str)
mx[:, :] = '.'
for line in raw[:kb]:
    y, x = line.strip().split(',')
    y, x = int(y), int(x)
    mx[x, y] = '#'

# Create graph
G = nx.Graph()
for r in range(S):
    for c in range(S):
        if mx[r, c] == '.':
            G.add_node((r, c))

# Add edges
for r, c in G.nodes:
    nbs = get_nbs(r, c, S)
    for r_nb, c_nb in nbs:
        if mx[r_nb, c_nb] == '.':
            G.add_edge((r, c), (r_nb, c_nb))

start = (0, 0)
end = (S - 1, S - 1)

path = nx.shortest_path(G, start, end)

sol = len(path) - 1
print(f"A ::: {sol}")

kb_start = 1024

def make_graph_by_kb(raw, S, kb):

    # Construct mx
    mx = np.zeros((S, S), dtype=str)
    mx[:, :] = '.'
    for line in raw[:kb]:
        y, x = line.strip().split(',')
        y, x = int(y), int(x)
        mx[x, y] = '#'

    # Create graph
    G = nx.Graph()
    for r in range(S):
        for c in range(S):
            if mx[r, c] == '.':
                G.add_node((r, c))

    # Add edges
    for r, c in G.nodes:
        nbs = get_nbs(r, c, S)
        for r_nb, c_nb in nbs:
            if mx[r_nb, c_nb] == '.':
                G.add_edge((r, c), (r_nb, c_nb))

    return G

start = (0, 0)
end = (S - 1, S - 1)

for byte in range(kb + 1, len(raw)):
    G = make_graph_by_kb(raw, S, byte)
    try:
        path = nx.shortest_path(G, start, end)
    except:
        break

sol = raw[byte - 1].strip()
print(f"B ::: {sol}")
