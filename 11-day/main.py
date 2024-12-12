data = [0, 5601550, 3914, 852, 50706, 68, 6, 645371]

data = {v: data.count(v) for v in data}

def process_item(n):
    L = len(str(n))
    if n == 0:
        res = [1]
    elif L % 2 == 0:
        res = [int(str(n)[:L//2]), int(str(n)[L//2:])]
    else:
        res = [2024*n]
    return res

def iterate(data):
    res = {}
    for value, n in data.items():
        new_items = process_item(value)
        for item in new_items:
            res[item] = res.get(item, 0) + n
    return res

for i in range(25):
    data = iterate(data)

sol = sum(data.values())
print(f"A ::: {sol}")

for i in range(50):
    data = iterate(data)

sol = sum(data.values())
print(f"B ::: {sol}")
