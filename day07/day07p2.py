from collections import Counter


def compute_cost(position_counter, target_position):
    cost = 0
    for position, count in position_counter.items():
        n = abs(position - target_position)
        cost += int((n * (n + 1) * count) / 2)
    return cost


with open("input.txt") as input:
    input_points = [int(_) for _ in input.readline().strip().split(",") if _]

min_pos = min(input_points)
max_pos = max(input_points)

print(f"{min_pos} -> {max_pos} with {len(input_points)} points")

start_pos_counter = Counter(input_points)

costs = {}
for pos in range(min_pos, max_pos + 1):
    cost = compute_cost(start_pos_counter, pos)
    costs[pos] = cost
#    print(f"{pos:>4} -> {cost}")

best = min(costs, key=costs.get)
print(f"{best} -> {costs[best]}")
