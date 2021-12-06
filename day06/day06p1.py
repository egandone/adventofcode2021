with open("input.txt") as input:
    ages = [int(_) for _ in input.readlines()[0].split(",")]

print(f"start - {ages}")
for day in range(1, 81):
    new_adds = 0
    for ix in range(len(ages)):
        if ages[ix] == 0:
            ages[ix] = 6
            new_adds += 1
        else:
            ages[ix] -= 1
    ages.extend([8] * new_adds)
    #    print(f"      day {day:>2} - {len(ages):>8} {ages}")
    print(f"      day {day:>2} - {len(ages):>8}")
