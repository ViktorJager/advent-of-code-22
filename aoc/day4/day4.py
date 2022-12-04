# AoC day 4

def read_file(path):
    with open(path) as f:
        return f.readlines()

def filter_newline(str):
    return str.replace("\n", "")

def fetch_data(path):
    return list(map(
        filter_newline,
        read_file(path)))

def split_section(s: str) -> str:
    range = s.split(',')
    return [range[0].split('-'), range[1].split('-')]

def get_section_pairs():
    data = fetch_data('./input/day4/input.txt')
    return list(map(split_section, data))

def setify(section):
    set_0 = [i for i in range(int(section[0][0]), int(section[0][1]) + 1)]
    set_1 = [i for i in range(int(section[1][0]), int(section[1][1]) + 1)]

    if len(set_0) > len(set_1):
        superset = set_0
        subset = set_1
    else:
        superset = set_1
        subset = set_0

    return superset, subset


def true_subset(superset, subset):
    return all(elem in superset for elem in subset)

def any_subset(superset, subset):
    return any(elem in superset for elem in subset)

sections = get_section_pairs()
listis_1 = []
listis_2 = []
for section in sections:
    superset, subset = setify(section)

    listis_1.append(true_subset(superset, subset))
    full_redundant_pairs = sum(listis_1)

    listis_2.append(any_subset(superset, subset))
    any_redundant_pairs = sum(listis_2)

print(f'Q1: {full_redundant_pairs}')
print(f'Q2: {any_redundant_pairs}')




# result =  all(elem in list1  for elem in list2)
a = 1