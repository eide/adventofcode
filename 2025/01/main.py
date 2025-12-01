data = []
with open("input.txt", encoding="utf-8") as f:
    data = f.read().strip().split("\n")

dial = 50
answer1 = 0
answer2 = 0

for r in data:
    prev = dial
    steps = int(r[1:])
    if r[0] == "R":
        spins, dial = divmod(dial + steps, 100)
    if r[0] == "L":
        spins, dial = divmod(dial - steps, 100)
        if prev == 0:
            answer2 -= 1
        if dial == 0:
            answer2 += 1

    answer2 += abs(spins)

    if dial == 0:
        answer1 += 1

print(f"part 1: {answer1}")
print(f"part 2: {answer2}")
