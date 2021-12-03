from collections import Counter

counters = None

with open("input.txt") as input:
    for n, line in enumerate(input.readlines()):
        line = line.strip()
        if not counters:
            counters = [Counter() for _ in range(len(line))]
        for i, d in enumerate(line):
            counters[i].update(d)

for c in counters:
    print(f"{c.most_common()}")

value1 = value2 = 0

for c in counters:
    value1 = value1 * 2 + int(c.most_common()[0][0])
    value2 = value2 * 2 + int(c.most_common()[1][0])
print(f"{value1} * {value2} = {value1 * value2}")
