with open("input.txt") as input:
    lines = [int(line.strip()) for line in input.readlines()]

trios = [t for t in zip(lines[:-2], lines[1:-1], lines[2:])]
trio_pairs = zip(trios[:-1], trios[1:])
increases = [pair for pair in trio_pairs if sum(pair[1]) > sum(pair[0])]
print(len(increases))
