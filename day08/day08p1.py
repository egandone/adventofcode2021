parsed_lines = []
with open("input.txt") as input:
    for line in input.readlines():
        (observations, numbers) = line.strip().split('|')
        observations = [o.strip() for o in observations.strip().split(' ')]
        numbers = [n.strip() for n in numbers.strip().split(' ')]
        parsed_lines.append((observations, numbers))

count = 0
for pair in parsed_lines:
    count += len([_ for _ in pair[1] if len(_) in (2,3,4,7)])
    print(f'{pair[0]} - {pair[1]}')

print(f'count = {count}')