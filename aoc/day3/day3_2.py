# AoC day 3

def read_file(path):
    with open(path) as f:
        return f.readlines()

def filter_newline(str):
    return str.replace("\n", "")

def fetch_data(path):
    return list(map(
        filter_newline,
        read_file(path)))


def find_common_item(r0, r1, r2):
    return set(r0) & set(r1) & set(r2)

def find_common_items(rucksacks):
    common_items = []
    for i in range(0, len(rucksacks), 3):
        common_items.append(find_common_item(
            rucksacks[i],
            rucksacks[i+1],
            rucksacks[i+2]
            ))
    return common_items

def prio_points(chr):
    return (ord(chr) - 96) if chr.islower() else (ord(chr) - 38)



rucksacks = fetch_data('./input/day3/input.txt')
common_items = find_common_items(rucksacks)

sum_priority = 0
for item in common_items:
    sum_priority += prio_points(list(item)[0])

print(f"Q2: {sum_priority}")
