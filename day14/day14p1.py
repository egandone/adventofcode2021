import pprint
from collections import Counter

pp = pprint.PrettyPrinter()


def do_iteration(sequence, inserts):
    new_sequence = [sequence[0]]
    c1 = sequence[0]
    for c2 in sequence[1:]:
        new_sequence.append(inserts[(c1, c2)])
        new_sequence.append(c2)
        c1 = c2
    return new_sequence


with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

sequence = list(lines[0])
insert_map = {}
for line in lines[2:]:
    key, value = line.split(" -> ")
    insert_map[tuple(key)] = value

print(f"Insert map: {insert_map}")
print(f"Tempate       : {sequence}")
for i in range(10):
    sequence = do_iteration(sequence, insert_map)
    #    print(f'After step {i+1}: {"".join(sequence)}')
    print(f"After step {i+1}: {len(sequence)}")

counter = Counter(sequence)
most = counter.most_common()[0]
least = counter.most_common()[-1]
print(f"{most} -> {least}")
diff = most[1] - least[1]
print(f"answer = {diff}")
