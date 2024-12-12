from collections import deque

raw = open('input.txt', 'r').readlines()[0].strip()

class DataBlock:
    def __init__(self, value, bid):
        self.value = int(value)
        self.bid = int(bid)
        self.is_free = False

    def __repr__(self):
        return f"Data[{self.value}, id={self.bid}]"

class FreeBlock:
    def __init__(self, value):
        self.value = int(value)
        self.bid = None
        self.is_free = True

    def __repr__(self):
        return f"Free[{self.value}]"

def expand_data(data):
    res = []
    for obj in data:
        if isinstance(obj, DataBlock):
            res += [str(obj.bid)]*obj.value
        else:
            res += ['.']*obj.value
    return res

def checksum(data):
    sum_ = 0
    for i, value in enumerate(data):
        if value != '.':
            sum_ += i*int(value)
    return sum_

data_blocks = []
for i, char in enumerate(raw):
    if i % 2 == 0:
        data_blocks.append(DataBlock(char, i // 2))
    else:
        data_blocks.append(FreeBlock(char))

data = expand_data(data_blocks)

pa = 0
pb = len(data) - 1

while pa <= pb:
    if data[pa] == '.':
        if data[pb] == '.':
            pb -= 1
        else:
            data[pa], data[pb] = data[pb], data[pa]
    else:
        pa += 1

sol = checksum(data)
print(f"A ::: {sol}")


def find_next_free(S, blocks):
    for i, b in enumerate(blocks):
        if b.is_free and b.value >= S:
            return i
    return -1

def find_block(bid, blocks):
    for i, b in enumerate(blocks):
        if b.bid == bid:
            return i
    return -1

block_memo = {b.bid: b.value for b in data_blocks if not b.is_free}
curr_block = max(block_memo)

while curr_block > 0:
    block_loc = find_block(curr_block, data_blocks)
    L = block_memo[curr_block]
    open_slot = find_next_free(L, data_blocks)
    if open_slot >= 0 and open_slot < block_loc:
        displaced_amt = data_blocks[open_slot].value - L
        data_blocks[open_slot] = data_blocks[block_loc]
        data_blocks[block_loc] = FreeBlock(L)
        data_blocks.insert(open_slot + 1, FreeBlock(displaced_amt))
    curr_block -= 1

sol = checksum(expand_data(data_blocks))
print(f"B ::: {sol}")
