def decode_observations(observations):
    one = [o for o in observations if len(o) == 2][0]
    seven = [o for o in observations if len(o) == 3][0]
    four = [o for o in observations if len(o) == 4][0]
    eight = [o for o in observations if len(o) == 7][0]
    three = [o for o in observations if len(o) == 5 and o.intersection(one) == one][0]

    seg1 = seven - one
    seg5_and_7 = eight - four - seg1

    two = [
        o
        for o in observations
        if len(o) == 5 and o.intersection(seg5_and_7) == seg5_and_7
    ][0]
    five = [o for o in observations if len(o) == 5 and o not in [two, three]][0]

    zero = [
        o
        for o in observations
        if len(o) == 6
        and o.intersection(seven.union(seg5_and_7)) == seven.union(seg5_and_7)
    ][0]
    six = five.union(seg5_and_7)
    nine = [o for o in observations if len(o) == 6 and o not in [zero, six]][0]

    return {
        frozenset(zero): 0,
        frozenset(one): 1,
        frozenset(two): 2,
        frozenset(three): 3,
        frozenset(four): 4,
        frozenset(five): 5,
        frozenset(six): 6,
        frozenset(seven): 7,
        frozenset(eight): 8,
        frozenset(nine): 9,
    }


parsed_lines = []
with open("input.txt") as input:
    for line in input.readlines():
        (observations, numbers) = line.strip().split("|")
        observations = [set(o.strip()) for o in observations.strip().split(" ")]
        numbers = [set(n.strip()) for n in numbers.strip().split(" ")]
        parsed_lines.append((observations, numbers))

sum = 0
count = 0
for pair in parsed_lines:
    mappings = decode_observations(pair[0])
    final_number = 0
    for number in pair[1]:
        n = mappings[frozenset(number)]
        final_number = 10 * final_number + int(n)
    print(f"{final_number}")
    sum += final_number
print(f"final sum = {sum}")
