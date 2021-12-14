import pprint
from collections import Counter
from collections import defaultdict

pp = pprint.PrettyPrinter()


def do_iteration(pairs, inserts):
    new_pairs = defaultdict(int)
    for pair, count in pairs.items():
        insert = inserts[pair]
        new_pair1 = pair[0] + insert
        new_pair2 = insert + pair[1]
        new_pairs[new_pair1] += count
        new_pairs[new_pair2] += count
    return new_pairs


with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

sequence = lines[0]
pairs = defaultdict(int)
for i in range(len(sequence) - 1):
    pairs[sequence[i : i + 2]] = 1
print(pairs)

insert_map = {}
for line in lines[2:]:
    key, value = line.split(" -> ")
    insert_map[key] = value

print(f"Insert map: {insert_map}")
print(f"Template      : {pairs}")
for i in range(40):
    pairs = do_iteration(pairs, insert_map)
    #    print(f'After step {i+1}: {"".join(sequence)}')
    print(f"After step {i+1}: {len(pairs)}")

letter_counter = defaultdict(int)
letter_counter[sequence[-1]] = 1
for pair, count in pairs.items():
    letter_counter[pair[0]] += count
most = max(letter_counter, key=letter_counter.get)
least = min(letter_counter, key=letter_counter.get)
print(f"{most}/{letter_counter[most]} -> {least}/{letter_counter[least]}")
diff = letter_counter[most] - letter_counter[least]
print(f"answer = {diff}")
