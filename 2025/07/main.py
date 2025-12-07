from collections import defaultdict

data = []
with open("input.txt") as f:
    data = f.read().splitlines()

splits = 0
s = data.pop(0).index("S")
beams = {s: 1}

for line in data:
    if "^" not in line:
        continue
    new_beams = defaultdict(int)
    for i, n in beams.items():
        if line[i] == "^":
            splits += 1
            new_beams[i - 1] += n
            new_beams[i + 1] += n
        else:
            new_beams[i] += n
    beams = new_beams

print(f"Part1: {splits}")
print(f"Part2: {sum(beams.values())}")
