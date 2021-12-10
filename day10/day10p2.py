from collections import deque


openings = {"(": ")", "{": "}", "[": "]", "<": ">"}
closing_costs = {")": 3, "]": 57, "}": 1197, ">": 25137}
fix_score = {")": 1, "]": 2, "}": 3, ">": 4}


def evaluate_line(l):
    parse_queue = deque()
    for c in l:
        if c in openings.keys():
            parse_queue.append(c)
        else:
            expected = openings[parse_queue.pop()]
            if c != expected:
                return closing_costs[c]
    return 0


def fix_line(l):
    parse_queue = deque()
    for c in l:
        if c in openings.keys():
            parse_queue.append(c)
        else:
            parse_queue.pop()
    endings = []
    while parse_queue:
        endings.append(openings[parse_queue.pop()])
    endings = "".join(endings)
    fixed_line = l + endings
    fixed_cost = evaluate_line(fixed_line)
    if fixed_cost != 0:
        raise ValueError("something wrong here")
    return endings


def compute_fix_score(l):
    score = 0
    for c in l:
        score = score * 5 + fix_score[c]
    return score


scores = []
with open("input.txt") as input:
    for line in input.readlines():
        line = line.strip()
        cost = evaluate_line(line)
        if cost == 0:
            endings = fix_line(line)
            score = compute_fix_score(endings)
            print(f"{endings} - {score}")
            scores.append(score)
scores.sort()
middle_score = scores[int((len(scores) - 1) / 2)]
print(f"middle score = {middle_score}")
