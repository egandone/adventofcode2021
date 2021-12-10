from collections import deque

openings = {"(": ")", "{": "}", "[": "]", "<": ">"}
closing_costs = {")": 3, "]": 57, "}": 1197, ">": 25137}
fix_score = {")": 1, "]": 2, "}": 3, ">": 4}


def evaluate_line(l: str) -> int:
    parse_queue = deque()
    for c in l:
        if c in openings.keys():
            # If it's the start of a block "push" it onto the queue
            parse_queue.append(c)
        else:
            # Otherwise if must be the close of a block.  In this
            # case we need to check if it matches the expected
            # close block character
            expected = openings[parse_queue.pop()]
            if c != expected:
                # If it doesn't match then lookup the
                # cost and return it
                return closing_costs[c]
    # If we get all the way through then we didn't have any
    # mismatches but this doesn't guarentee that the string is
    # valid - i.e., there might still be open blocks
    return 0


def fix_line(l: str) -> str:
    parse_queue = deque()

    # Iterate over the input, which is assumed
    # to _not_ have any mimatches.  We then just
    # use a stack to keep track of currently
    # open code blocks.
    for c in l:
        if c in openings.keys():
            parse_queue.append(c)
        else:
            parse_queue.pop()
    # To find the required endings we just need
    # to pop off all the unclosed blocks and append
    # the appropriate closing charater
    endings = []
    while parse_queue:
        endings.append(openings[parse_queue.pop()])
    # turn it into a simple string
    endings = "".join(endings)
    # The follow will double check that the fixed version of the
    # string passes the validation test.  Used this during my initial
    # testing because I wasn't 100% the logic was right :)
    #    fixed_line = l + endings
    #    fixed_cost = evaluate_line(fixed_line)
    #    if fixed_cost != 0:
    #        raise ValueError("something wrong here")
    return endings


def compute_fix_score(l: str) -> int:
    score = 0
    for c in l:
        score = score * 5 + fix_score[c]
    return score


scores = []
with open("input.txt") as input:
    for line in input.readlines():
        line = line.strip()
        cost = evaluate_line(line)
        # Only investigate lines that pass validation (i.e., cost is 0)
        if cost == 0:
            endings = fix_line(line)
            score = compute_fix_score(endings)
            # print(f"{endings} - {score}")
            scores.append(score)
scores.sort()
middle_score = scores[int((len(scores) - 1) / 2)]
print(f"Total of {len(scores)} fixed lines -> middle score = {middle_score}")
