data = []
with open("input.txt", encoding="utf-8") as f:
    data = f.read().strip().split("\n")

total1 = 0
for line in data:
    high = sorted(line[:-1], reverse=True)[0]
    rest = line[line.index(high) + 1:]
    low = sorted(rest, reverse=True)[0]
    total1 += int(f"{high}{low}")

print(f"Part1: {total1}")

total2 = 0
for line in data:
    batteries = ""
    high = sorted(line[:-12], reverse=True)[0]
    batteries += high
    rest = line[line.index(high) + 1:]
    while len(batteries) < 12:
        high = sorted(rest[:len(rest) - 12 + 1 + len(batteries)], reverse=True)[0]
        batteries += high
        rest = rest[rest.index(high) + 1:]
    batteries += rest[:12-len(batteries)]
    total2 += int(batteries)

print(f"Part2: {total2}")
