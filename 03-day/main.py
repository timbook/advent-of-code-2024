import re

raw = open('input.txt', 'r').readlines()
data = [line.strip() for line in raw]

pattern = "mul\((\d{1,3}),(\d{1,3})\)"

total = 0
for line in data:
    total += sum([int(a)*int(b) for a, b in re.findall(pattern, line)])

print(f"A ::: {total}")

p1 = "(mul)\((\d{1,3}),(\d{1,3})\)"
p2 = "(don\'t|do)\(\)"
pattern = f"{p1}|{p2}"

def process_mul(op):
    _, a, b, _ = op
    return int(a)*int(b)

total = 0

enabled = True
for line in data:
    ops = re.findall(pattern, line)
    for op in ops:
        if enabled and 'mul' in op:
            total += process_mul(op)
        elif op[-1] == 'do':
            enabled = True
        elif op[-1] == 'don\'t':
            enabled = False

print(f"B ::: {total}")
