ranges = []
ids = []
with open("input.txt") as f:
    ranges, ids = map(lambda x: x.split("\n"), f.read().strip().split("\n\n"))

ids = [int(i) for i in ids]
pool = sorted([tuple([int(n) for n in r.split("-")]) for r in ranges])

ranges = []
l1, h1 = pool.pop(0)
while True:
    if len(pool) <= 0:
        break
    l2, h2 = pool.pop(0)
    if l2 <= h1:
        h1 = max(h1, h2)
    else:
        ranges.append((l1, h1))
        l1, h1 = l2, h2
ranges.append((l1, h1))

fresh_ids = []
fresh = []
for i in ids:
    for low,high in ranges:
        if low <= i and high >= i:
            fresh.append(i)
            break

print(f"Part 1: {len(fresh)}")

count = 0
for l,h in ranges:
    count += (h + 1) - l

print(f"Part 2: {count}")
