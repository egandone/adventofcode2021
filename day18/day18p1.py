from snailfish import parse_expression, reduce, split_string


with open("input.txt") as input:
    lines = [line.strip() for line in input.readlines()]


expr = parse_expression(lines[0])
for line in lines[1:]:
    expr = expr.add(parse_expression(line))
    expr = reduce(expr)

print(expr.magnitude())
