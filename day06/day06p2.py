def get_children(s):
    ages = [s]
    for day in range(1, 129):
        new_adds = 0
        for ix in range(len(ages)):
            if ages[ix] == 0:
                ages[ix] = 6
                new_adds += 1
            else:
                ages[ix] -= 1
        ages.extend([8] * new_adds)

    return ages


lookups = {}
for age in range(0, 9):
    lookups[age] = get_children(age)

with open("input.txt") as input:
    ages = [int(_) for _ in input.readlines()[0].split(",")]

ages128 = []
for x in ages:
    ages128.extend(lookups.get(x))
print(f"After 128 steps -> {len(ages128)}")

total_at_256 = 0
for x in ages128:
    total_at_256 += len(lookups.get(x))
print(f"After 256 steps -> {total_at_256}")
