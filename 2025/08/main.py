from uuid import uuid4
from math import sqrt, pow, prod

data = set()
with open("input.txt") as f:
    data = {tuple([int(c) for c in line.split(",")]) for line in f.read().splitlines()}

def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))

distances = {}
for l1 in data:
    for l2 in data:
        if l1 == l2:
            continue
        d = distance(l1, l2)
        if d not in distances:
            distances[d] = []
        distances[d] = (l1, l2)

ck = {}
circuits = {}

for d in data:
    uuid = uuid4()
    ck[d] = uuid
    circuits[uuid] = [d]

part1 = 0
keys = sorted(distances.keys())
for i, key in enumerate(keys):
    if i == 1000:
        part1 = prod(sorted([len(values) for values in circuits.values()])[-3:])
    s1, s2 = distances[key]
    id1 = ck[s1]
    id2 = ck[s2]
    if id1 == id2:
        continue
    circuits[id1] += circuits[id2]
    for c in circuits[id2]:
        ck[c] = id1
    del circuits[id2]
    if len(circuits.keys()) == 1:
        break

print(f"Part1: {part1}")
print(f"Part2: {s1[0] * s2[0]}")
