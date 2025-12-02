import re

data = []
with open("input.txt", encoding="utf-8") as f:
    data = f.read().strip().replace("\n", "").split(",")

part1 = 0
part2 = 0

for ids in data:
    low, high = ids.split("-")
    invalid = []
    for i in range(int(low), int(high) + 1):
        number = str(i)
        length = len(number)
        middle = length // 2
        for split in range(middle, 0, -1):
            prefix = number[:split]
            match = re.match(rf"^({prefix})+$", number)
            if match and i not in invalid:
                invalid.append(i)
                part2 += i

        if length % 2 == 0:
            first = number[:middle]
            last = number[middle:]
            if first == last:
                part1 += i

print(f"Part1: {part1}")
print(f"Part2: {part2}")
