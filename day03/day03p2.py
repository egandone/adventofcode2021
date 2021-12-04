def least_common(numbers, position):
    m = most_common(numbers, position)
    return "1" if m == "0" else "0"


def most_common(numbers, position):
    one_count = len([n for n in numbers if n[position] == "1"])
    zero_count = len(numbers) - one_count
    return "1" if one_count >= zero_count else "0"


def filter_to_one(l, function):
    p = 0
    while len(l) > 1:
        c = function(l, p)
        l = [n for n in l if n[p] == c]
        p += 1
    if len(l) != 1:
        raise ValueError("Failed reducing list to just one")
    return l[0]


with open("input.txt") as input:
    numbers = [line.strip() for line in input.readlines()]

value1 = filter_to_one(numbers, most_common)
value1 = int(value1, 2)

value2 = filter_to_one(numbers, least_common)
value2 = int(value2, 2)

print(f"{value1} * {value2} = {value1 * value2}")
