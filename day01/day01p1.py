
with open("input.txt") as input:
    lines = [int(line.strip()) for line in input.readlines()]

pairs = zip(lines[:-1], lines[1:])
increases = [pair for pair in pairs if pair[1] > pair[0]]
print(len(increases))