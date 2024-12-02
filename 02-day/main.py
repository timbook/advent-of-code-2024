import numpy as np

raw = open('input.txt', 'r').readlines()
data = [[int(i) for i in line.strip().split()] for line in raw]


def is_mono(seq):
    seq_sorted = sorted(seq)
    is_inc = all([a == b for a, b in zip(seq, seq_sorted)])
    is_dec = all([a == b for a, b in zip(seq, seq_sorted[::-1])])
    return is_inc | is_dec

def step_cond(seq):
    diffs = [abs(a - b) for a, b in zip(seq[:-1], seq[1:])]
    return all([1 <= d <= 3 for d in diffs])

sol = len([1 for seq in data if is_mono(seq) and step_cond(seq)])
print(f"A ::: {sol}")

count = 0
for seq in data:
    for i, val in enumerate(seq):
        seq_i = seq[:i] + seq[i+1:]
        if is_mono(seq_i) and step_cond(seq_i):
            count += 1
            break

print(f"B ::: {count}")
