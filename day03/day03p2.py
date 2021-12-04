def least_common(numbers, position):
    m = most_common(numbers, position)
    return "1" if m == "0" else "0"


def most_common(numbers, position):
    one_count = len([n for n in numbers if n[position] == "1"])
    zero_count = len(numbers) - one_count
    return "1" if one_count >= zero_count else "0"


with open("input.txt") as input:
    list1 = [l.strip() for l in input.readlines()]
list2 = list1.copy()

p = 0
while len(list1) > 1:
    c = most_common(list1, p)
    list1 = [n for n in list1 if n[p] == c]
    p += 1
if len(list1) != 1:
    raise ValueError("list1 is empty")
value1 = int(list1[0], 2)

p = 0
while len(list2) > 1:
    c = least_common(list2, p)
    list2 = [n for n in list2 if n[p] == c]
    p += 1
if len(list2) != 1:
    raise ValueError("list2 is empty")
value2 = int(list2[0], 2)

print(f"{value1} * {value2} = {value1 * value2}")
