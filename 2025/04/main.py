data = {}
with open("input.txt") as f:
    data = dict([((y, x), c) for y, line in enumerate(f.readlines()) for x, c in enumerate(line.strip())])
ymax, xmax = max(data.keys())

movements = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]

def rollup():
    accessible = 0
    nd = {}
    for y in range(0, ymax + 1):
        for x in range(0, xmax + 1):
            curr = data[(y, x)]
            nd[(y, x)] = curr
            if curr != "@":
                continue
            rollcount = 0
            for (my, mx) in movements:
                dy = y + my
                dx = x + mx
                if data.get((dy, dx)) == "@":
                    rollcount += 1
            if rollcount < 4:
                accessible += 1
                nd[(y, x)] = "."
    return (accessible, nd)

print(f"Part1: {rollup()[0]}")

total = 0
while True:
    rolls, data = rollup()
    total += rolls
    if rolls == 0:
        break

print(f"Part2: {total}")
