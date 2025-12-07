import re

data = []
with open("input.txt") as f:
    data = f.read().splitlines()

def part1():
    spaces = re.compile(r"\s+")
    lines = [spaces.sub(" ", line).strip().split(" ") for line in data]

    ops = lines.pop()
    totals = []
    for line in lines:
        for i, num in enumerate(line):
            if len(totals) <= i:
                totals.append(int(num))
            elif ops[i] == "+":
                totals[i] += int(num)
            elif ops[i] == "*":
                totals[i] *= int(num)

    print(f"Part1: {sum(totals)}")

def part2():
    ops = data.pop().strip("\n")
    i = -1
    totals = []
    curr_op = ""
    for j, op in enumerate(ops):
        num = ""
        if op != " ":
            curr_op = op
            i += 1
        for line in data:
            num = (num + line[j]).strip()
        if num != "":
            if len(totals) <= i:
                totals.append(int(num))
            elif curr_op == "+":
                totals[i] += int(num)
            elif curr_op == "*":
                totals[i] *= int(num)

    print(f"Part2: {sum(totals)}")

part1()
part2()
