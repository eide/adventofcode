data = []
with open("input.txt", encoding="utf-8") as f:
    data = f.read().strip().split("\n")

def jolt(length):
    joltage = 0

    for line in data:
        batteries = ""
        pos = 0
        while len(batteries) < length:
            search = len(line) - (length - 1 - len(batteries))
            high = max(line[pos:search])
            pos = line.index(high, pos) + 1
            batteries += high
        joltage += int(batteries)

    return joltage

print(f"Part1: {jolt(2)}")
print(f"Part2: {jolt(12)}")
