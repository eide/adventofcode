from collections import defaultdict
from itertools import combinations
from math import inf

data = []
with open("input.txt") as f:
    for line in f.read().splitlines():
        machine = line.split(" ")
        data.append((
            tuple(1 if l == "#" else 0 for l in machine[0][1:-1]),
            [[int(b) for b in button[1:-1].split(",")] for button in machine[1:-1]],
            tuple(int(j) for j in machine[-1][1:-1].split(",")),
        ))

def button_combos(buttons):
    presses = range(len(buttons))
    for i in range(len(buttons) + 1):
        yield from combinations(presses, i)

part1 = 0
part2 = 0

for lights, buttons, joltage in data:
    combos = button_combos(buttons)

    power_to_buttons = defaultdict(list)
    buttons_to_power = {}

    for combo in combos:
        joltage_supply = [len([1 for b in combo if j in buttons[b]]) for j in range(len(joltage))]
        parity = tuple(j % 2 for j in joltage_supply)
        power_to_buttons[parity] += [combo]
        buttons_to_power[combo] = joltage_supply

    part1 += min(len(btns) for btns in power_to_buttons[lights])

    def press_buttons_like_a_maniac(power_target):
        if min(power_target) < 0:
            return inf
        if sum(power_target) == 0:
            return 0

        ans = inf
        parity = tuple(j % 2 for j in power_target)
        for btns in power_to_buttons[parity]:
            nxt = tuple((j - js) // 2 for j, js in zip(power_target, buttons_to_power[btns]))
            ans = min(ans, len(btns) + 2 * press_buttons_like_a_maniac(nxt))
        return ans

    part2 += press_buttons_like_a_maniac(joltage)

print(f"{part1= }")
print(f"{part2= }")
