from snailfish import parse_expression, reduce, split_string


with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]

max_magnitude = 0
for l1 in range(len(lines)):
    for l2 in range(len(lines)):
        expr = parse_expression(lines[l1])
        expr = expr.add(parse_expression(lines[l2]))
        expr = reduce(expr)
        magnitude = expr.magnitude()
        if magnitude > max_magnitude:
            max_magnitude = magnitude

print(max_magnitude)
