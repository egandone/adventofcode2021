from collections import Counter

with open("input.txt") as input:
    ages = [int(_) for _ in input.readlines()[0].split(",")]

day_counter = {i:0 for i in range(9)}
for age, count in Counter(ages).items():
    day_counter[age] = count

for day in range(1,257):
    next_day_counter = dict()
    for p in range(1,9):
        next_day_counter[p-1] = day_counter[p]
    next_day_counter[6] += day_counter[0]
    next_day_counter[8] = day_counter[0]
    day_counter = next_day_counter
    total_count = sum(day_counter.values())
    print(f'after {day:>4} days - {total_count}')
