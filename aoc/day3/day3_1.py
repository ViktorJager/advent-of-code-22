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


def split_bag_compartments(str):
    midpoint = int(len(str) / 2)
    return [str[0:midpoint], str[midpoint:]]

def find_common_item(rucksack):
    return set(rucksack[0]) & set(rucksack[1])

def find_common_items(rucksacks):
    common_items = []
    for r in rucksacks:
        compartments = split_bag_compartments(r)
        common_items.append(find_common_item(compartments))
    return common_items

rucksacks = fetch_data('./input/day3/input.txt')
common_items = find_common_items(rucksacks)


def prio_points(chr):
    return (ord(chr) - 96) if chr.islower() else (ord(chr) - 38)

sum_priority = 0
for item in common_items:
    sum_priority += prio_points(list(item)[0])


print(f"Q1: {sum_priority}")