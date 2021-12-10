from collections import deque


openings = {"(": ")", "{": "}", "[": "]", "<": ">"}
closing_costs = {")": 3, "]": 57, "}": 1197, ">": 25137}


def evaluate_line(l):
    parse_queue = deque()
    for c in l.strip():
        if c in openings.keys():
            parse_queue.append(c)
        else:
            expected = openings[parse_queue.pop()]
            if c != expected:
                print(f"{l} - Expected {expected}, but found {c} instead")
                return closing_costs[c]
    return 0


total_cost = 0
with open("input.txt") as input:
    for line in input.readlines():
        cost = evaluate_line(line.strip())
        total_cost += cost
print(f"total cost = {total_cost}")
