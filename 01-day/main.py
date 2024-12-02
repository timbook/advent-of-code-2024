import numpy as np
import pandas as pd

raw = open('input.txt', 'r').readlines()
mx = np.array([line.strip().split() for line in raw])
df = pd.DataFrame(mx, columns=list('ab')).astype(int)

a_sorted = df.sort_values('a').a.reset_index(drop=True)
b_sorted = df.sort_values('b').b.reset_index(drop=True)
df_sorted = pd.DataFrame({'a': a_sorted, 'b': b_sorted})

sol = (df_sorted.a - df_sorted.b).abs().sum()

print(f"A ::: {sol}")

sol = 0
for value in df.a:
    if value in df.b.values:
        z = df.b[df.b  == value].shape[0]
        sol += value*z

print(f"B ::: {sol}")
