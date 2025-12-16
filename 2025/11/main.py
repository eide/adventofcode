from functools import cache

data = {}
with open("input.txt") as f:
    data = {k: v.split() for k, v in (line.split(": ") for line in f.read().splitlines())}

@cache
def find_out(device, dac, fft):
    if device == "out":
        return fft & dac
    if device == "dac":
        dac = 1
    if device == "fft":
        fft = 1

    ways_out = 0
    for device in data[device]:
        ways_out += find_out(device, dac, fft)
    return ways_out


print("Part1", find_out("you", 1, 1))
print("Part2", find_out("svr", 0, 0))
