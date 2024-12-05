file = 'input.txt'

raw = open(file, 'r').readlines()
raw_rules = [line.strip() for line in raw if '|' in line]
raw_update = [line.strip() for line in raw if ',' in line]

def str_to_rule(s):
    a, b = s.split('|')
    return int(a), int(b)

def str_to_update(s):
    list_ = s.split(',')
    return [int(i) for i in list_]

rules = [str_to_rule(r) for r in raw_rules]
updates = [str_to_update(u) for u in raw_update]

def is_update_good(update, rules):
    for i, item in enumerate(update):
        prereqs = update[:i]
        postreqs = update[i+1:]

        for req in prereqs:
            rule = f"{req}|{item}"
            if rule not in raw_rules:
                return False
            
        for req in postreqs:
            rule = f"{item}|{req}"
            if rule not in raw_rules:
                return False

    return True

def get_middle(v):
    L = len(v)
    return v[L // 2]

good_updates = [update for update in updates if is_update_good(update, rules)]
middles = [get_middle(u) for u in good_updates]
sol = sum(middles)
print(f"A ::: {sol}")

bad_updates = [update for update in updates if not is_update_good(update, rules)]

def swap_sort(update):
    arr = update.copy()
    L = len(arr)
    for i in range(L):
        for j in range(i + 1, L):
            if f"{arr[i]}|{arr[j]}" not in raw_rules:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

corrected_updates = [swap_sort(u) for u in bad_updates]
middles = [get_middle(u) for u in corrected_updates]
sol = sum(middles)
print(f"B ::: {sol}")
