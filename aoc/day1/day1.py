from util.filereader import read_file

lines = read_file('./input/day1/input.txt')
# lines = read_file('./input/day1/testdata.txt')
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