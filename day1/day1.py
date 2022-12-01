


def read_file(path):
    with open(path) as f:
        return f.readlines()


lines = read_file('./day1/input1.txt')
# lines = read_file('./day1/input1-test.txt')
# print(lines)

res = []
for sub in lines:
    res.append(sub.replace("\n", ""))

# print(res)

i = 0
calories = [0]
for x in res:
    if not x:
        i = i + 1
        calories.append(0)
        continue
    calories[i] = calories[i] + int(x)

# print(calories)

calories.sort(reverse = True)
print(f"Q1: {calories[0]}")
print(f"Q2: {sum(calories[0:3])}")