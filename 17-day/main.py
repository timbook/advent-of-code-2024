# Sample data
#  reg = {'A': 729, 'B': 0, 'C': 0}
#  prog_raw = '0,1,5,4,3,0'
#  prog = [int(i) for i in prog_raw.split(',')]

# Full data
reg = {'A': 30553366, 'B': 0, 'C': 0}
prog_raw = '2,4,1,1,7,5,4,7,1,4,0,3,5,5,3,0'
prog = [int(i) for i in prog_raw.split(',')]

def lit_to_combo(reg, literal):
    return {
        0: 0, 1: 1, 2: 2, 3: 3,
        4: reg['A'],
        5: reg['B'],
        6: reg['C']
    }[literal]

# Op 0
def adv(reg, literal):
    combo = lit_to_combo(reg, literal)
    reg['A'] = reg['A'] // (2**combo) 

# Op 1
def bxl(reg, literal):
    reg['B'] = reg['B'] ^ literal

# Op 2
def bst(reg, literal):
    combo = lit_to_combo(reg, literal)
    reg['B'] = combo % 8

# Op 3
def jnz(reg, literal):
    return literal

# Op 4
def bxc(reg, literal):
    reg['B'] = reg['B'] ^ reg['C']

# Op 5
def out(reg, literal):
    combo = lit_to_combo(reg, literal)
    return combo % 8

# Op 6
def bdv(reg, literal):
    combo = lit_to_combo(reg, literal)
    reg['B'] = int(reg['A'] / 2**combo)

# Op 7
def cdv(reg, literal):
    combo = lit_to_combo(reg, literal)
    reg['C'] = int(reg['A'] / 2**combo)

op_codes = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

def run_program(prog, reg):
    ptr = 0
    output = []
    while 0 <= ptr < len(prog):
        inst = prog[ptr]
        literal = prog[ptr + 1]

        if inst == 3:
            if reg['A'] == 0:
                ptr += 2
            else:
                ptr = op_codes[inst](reg, literal)
        elif inst == 5:
            out_ = op_codes[inst](reg, literal)
            output.append(out_)
            ptr += 2
        else:
            op_codes[inst](reg, literal)
            ptr += 2

    return output

o = run_program(prog, reg)
sol = ','.join([str(i) for i in o])
print(f"A ::: {sol}")
