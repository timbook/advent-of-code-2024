import numpy as np

raw = open('input.txt', 'r').readlines()
mx = np.array([list(line.strip()) for line in raw])

def count_rows(mx):
    right = np.sum([''.join(row).count('XMAS') for row in mx])
    rev = np.sum([''.join(row[::-1]).count('XMAS') for row in mx])
    return right + rev

def count_diag(mx):
    R, C = mx.shape
    xs, ys = np.where(mx == 'X')
    count = 0
    for x, y in zip(xs, ys):
        x_pos = x + np.arange(4)
        x_neg = x - np.arange(4)
        y_pos = y + np.arange(4)
        y_neg = y - np.arange(4)

        xn_good = np.all(0 <= x_neg)
        yn_good = np.all(0 <= y_neg)
        xp_good = np.all(x_pos < R)
        yp_good = np.all(y_pos < C)

        if xp_good and yp_good and ''.join(mx[x_pos, y_pos]) == 'XMAS':
            count += 1

        if xn_good and yn_good and ''.join(mx[x_neg, y_neg]) == 'XMAS':
            count += 1

        if xn_good and yp_good and ''.join(mx[x_neg, y_pos]) == 'XMAS':
            count += 1

        if xp_good and yn_good and ''.join(mx[x_pos, y_neg]) == 'XMAS':
            count += 1

    return count

sol = count_rows(mx) + count_rows(mx.T) + count_diag(mx)
print(f"A ::: {sol}")

def count_mas(mx):
    R, C = mx.shape
    count = 0
    xs, ys = np.where(mx == 'A')
    for x, y in zip(xs, ys):
        if 1 <= x <= R - 2 and 1 <= y <= C - 2:
            nw = mx[x - 1, y - 1]
            ne = mx[x - 1, y + 1]
            sw = mx[x + 1, y - 1]
            se = mx[x + 1, y + 1]
            comb = nw + ne + sw + se
            if comb in ['MMSS', 'MSMS', 'SMSM', 'SSMM']:
                count += 1

    return count

sol = count_mas(mx)
print(f"B ::: {sol}")
