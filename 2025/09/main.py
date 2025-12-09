data = []
with open("input.txt") as f:
    data = [[int(x) for x in line.split(",")] for line in f.read().splitlines()]

largest = -1
for x1,y1 in data:
    for x2,y2 in data:
        if x1 == x2 and y1 == y2:
            continue
        dx = abs(x1 - x2) + 1
        dy = abs(y1 - y2) + 1
        a = dx * dy
        if a > largest:
            largest = a
print(largest)
