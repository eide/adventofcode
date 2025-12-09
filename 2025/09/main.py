data = []
with open("input.txt") as f:
    data = [[int(x) for x in line.split(",")] for line in f.read().splitlines()]

xset = set()
yset = set()
for x, y in data:
    xset.add(x)
    xset.add(x + 1)
    yset.add(y)
    yset.add(y + 1)

xs = sorted(xset)
ys = sorted(yset)

xmap = {x: i for i, x in enumerate(xs)}
ymap = {y: i for i, y in enumerate(ys)}

boundary_grid = [[0 for _ in ys] for _ in xs]

n = len(data)
for i, (x1, y) in enumerate(data):
    x2, _ = data[(i + 1) % n]
    x1, x2 = sorted([xmap[x1], xmap[x2]])
    y = ymap[y]
    if x1 != x2:
        boundary_grid[x1][y] |= 1
        boundary_grid[x2][y] |= 2
        for x in range(x1 + 1, x2):
            boundary_grid[x][y] |= 3

interior_grid = [[False for _ in ys] for _ in xs]
for i, row in enumerate(boundary_grid):
    inside = 0
    for j, cell in enumerate(row):
        interior_grid[i][j] = inside > 0 or cell > 0
        inside ^= cell

prefix_sums = [[0] * (len(ys) + 1) for _ in range(len(xs) + 1)]
for i, row in enumerate(interior_grid):
    for j, cell in enumerate(row):
        prefix_sums[i + 1][j + 1] = int(cell) + prefix_sums[i][j + 1] + prefix_sums[i + 1][j] - prefix_sums[i][j]

a1, a2 = 0, 0
part1, part2 = -1, -1

for i, (x1,y1) in enumerate(data):
    for j, (x2,y2) in enumerate(data[:i]):
        xmin, xmax = sorted([x1, x2])
        ymin, ymax = sorted([y1, y2])
        rect_area = (xmax - xmin + 1) * (ymax - ymin + 1)
        part1 = max(part1, rect_area)

        xi1, xi2 = xmap[xmin], xmap[xmax]
        yi1, yi2 = ymap[ymin], ymap[ymax]
        cell_count = (xi2 - xi1 + 1) * (yi2 - yi1 + 1)
        total = prefix_sums[xi2 + 1][yi2 + 1] - prefix_sums[xi2 + 1][yi1] - prefix_sums[xi1][yi2 + 1] + prefix_sums[xi1][yi1]
        if total == cell_count:
            rect_area = (xs[xi2] - xs[xi1] + 1) * (ys[yi2] - ys[yi1] + 1)
            part2 = max(part2, rect_area)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
