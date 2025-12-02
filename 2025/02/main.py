import re

data = []
with open("input.txt", encoding="utf-8") as f:
    data = f.read().strip().replace("\n", "").split(",")

part1 = 0
part2 = 0

re1 = re.compile(r"^(\d+)\1$")
re2 = re.compile(r"^(\d+)\1+$")

for ids in data:
    low, high = ids.split("-")
    for i in range(int(low), int(high) + 1):
        number = str(i)

        m1 = re1.match(number)
        if m1:
            part1 += i

        m2 = re2.match(number)
        if m2:
            part2 += i

print(f"Part1: {part1}")
print(f"Part2: {part2}")
