from snailfish import parse_expression, reduce, split_string


def test_split_string():
    (l, r) = split_string("[1,2]")
    assert l == "1" and r == "2"

    (l, r) = split_string("[[1,2],3]")
    assert l == "[1,2]" and r == "3"

    (l, r) = split_string("[9,[8,7]]")
    assert l == "9" and r == "[8,7]"

    (l, r) = split_string("[[1,9],[8,5]]")
    assert l == "[1,9]" and r == "[8,5]"

    (l, r) = split_string("[[[[1,2],[3,4]],[[5,6],[7,8]]],9]")
    assert l == "[[[1,2],[3,4]],[[5,6],[7,8]]]" and r == "9"

    (l, r) = split_string("[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]")
    assert l == "[[9,[3,8]],[[0,9],6]]" and r == "[[[3,7],[4,9]],3]"

    (l, r) = split_string(
        "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    )
    assert l == "[[[1,3],[5,3]],[[1,3],[8,7]]]" and r == "[[[4,9],[6,9]],[[8,2],[7,3]]]"


def test_parse_expression():
    expr = parse_expression("[1,2]")
    assert len(expr.get_nodes()) == 1

    expr = parse_expression("[9,[8,7]]")
    assert len(expr.get_nodes()) == 2

    expr = parse_expression("[[1,9],[8,5]]")
    assert len(expr.get_nodes()) == 3

    expr = parse_expression("[[[[1,2],[3,4]],[[5,6],[7,8]]],9]")
    all_nodes = expr.get_nodes()
    assert len(all_nodes) == 8
    assert all_nodes[0].left == 1 and all_nodes[0].right == 2
    assert all_nodes[2].left == 3 and all_nodes[2].right == 4
    assert all_nodes[4].left == 5 and all_nodes[4].right == 6
    assert all_nodes[6].left == 7 and all_nodes[6].right == 8
    assert all_nodes[7].right == 9

    expr = parse_expression(
        "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"
    )
    assert len(expr.get_nodes()) == 15
    assert str(expr) == "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"


def test_depth():
    expr = parse_expression("[[[[[9,8],1],2],3],4]")
    nodes = expr.get_nodes()
    assert len(nodes) == 5
    assert nodes[0].depth() == 4
    assert nodes[1].depth() == 3
    assert nodes[2].depth() == 2
    assert nodes[3].depth() == 1
    assert nodes[4].depth() == 0

    expr = parse_expression("[7,[6,[5,[4,[3,2]]]]]")
    nodes = expr.get_nodes()
    assert len(nodes) == 5
    assert nodes[4].depth() == 4
    assert nodes[3].depth() == 3
    assert nodes[2].depth() == 2
    assert nodes[1].depth() == 1
    assert nodes[0].depth() == 0


def test_reduce():
    expr = parse_expression("[[[[[9,8],1],2],3],4]")
    expr = reduce(expr)
    assert str(expr) == "[[[[0,9],2],3],4]"

    expr = parse_expression("[7,[6,[5,[4,[3,2]]]]]")
    expr = reduce(expr)
    assert str(expr) == "[7,[6,[5,[7,0]]]]"

    expr = parse_expression("[[6,[5,[4,[3,2]]]],1]")
    expr = reduce(expr)
    assert str(expr) == "[[6,[5,[7,0]]],3]"

    expr = parse_expression("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
    expr = reduce(expr)
    assert str(expr) == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

    expr = parse_expression("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    expr = reduce(expr)
    assert str(expr) == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

    expr = parse_expression("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
    expr = reduce(expr)
    assert str(expr) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

    expr = parse_expression("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
    expr = reduce(expr)
    assert str(expr) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"


def test_example1():
    exprs = ["[1,1]", "[2,2]", "[3,3]", "[4,4]"]
    expr = parse_expression(exprs[0])
    for s in exprs[1:]:
        expr = expr.add(parse_expression(s))
        expr = reduce(expr)
    assert str(expr) == "[[[[1,1],[2,2]],[3,3]],[4,4]]"


def test_example2():
    exprs = ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]"]
    expr = parse_expression(exprs[0])
    for s in exprs[1:]:
        expr = expr.add(parse_expression(s))
        expr = reduce(expr)
    assert str(expr) == "[[[[3,0],[5,3]],[4,4]],[5,5]]"


def test_example3():
    exprs = ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"]
    expr = parse_expression(exprs[0])
    for s in exprs[1:]:
        expr = expr.add(parse_expression(s))
        expr = reduce(expr)
    assert str(expr) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"


def test_example4():
    exprs = [
        "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
        "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
        "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
        "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
        "[7,[5,[[3,8],[1,4]]]]",
        "[[2,[2,2]],[8,[8,1]]]",
        "[2,9]",
        "[1,[[[9,3],9],[[9,0],[0,7]]]]",
        "[[[5,[7,4]],7],1]",
        "[[[[4,2],2],6],[8,7]]",
    ]
    expr = parse_expression(exprs[0])
    expr = expr.add(parse_expression(exprs[1]))
    expr = reduce(expr)
    assert str(expr) == "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"

    expr = expr.add(parse_expression(exprs[2]))
    expr = reduce(expr)
    assert str(expr) == "[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]"

    expr = expr.add(parse_expression(exprs[3]))
    expr = reduce(expr)
    assert str(expr) == "[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]"

    expr = expr.add(parse_expression(exprs[4]))
    expr = reduce(expr)
    assert str(expr) == "[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]"

    expr = expr.add(parse_expression(exprs[5]))
    expr = reduce(expr)
    assert str(expr) == "[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]"

    expr = expr.add(parse_expression(exprs[6]))
    expr = reduce(expr)
    assert str(expr) == "[[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]"

    expr = expr.add(parse_expression(exprs[7]))
    expr = reduce(expr)
    assert str(expr) == "[[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]"

    expr = expr.add(parse_expression(exprs[8]))
    expr = reduce(expr)
    assert str(expr) == "[[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]"

    expr = expr.add(parse_expression(exprs[9]))
    expr = reduce(expr)
    assert str(expr) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"


def test_magnitude():
    expr = parse_expression("[9,1]")
    assert expr.magnitude() == 29

    expr = parse_expression("[1,9]")
    assert expr.magnitude() == 21

    expr = parse_expression("[[9,1],[1,9]]")
    assert expr.magnitude() == 129

    expr = parse_expression("[[1,2],[[3,4],5]]")
    assert expr.magnitude() == 143

    expr = parse_expression("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
    assert expr.magnitude() == 1384

    expr = parse_expression("[[[[1,1],[2,2]],[3,3]],[4,4]]")
    assert expr.magnitude() == 445
    expr = parse_expression("[[[[3,0],[5,3]],[4,4]],[5,5]]")
    assert expr.magnitude() == 791.0
    expr = parse_expression("[[[[5,0],[7,4]],[5,5]],[6,6]]")
    assert expr.magnitude() == 1137.0
    expr = parse_expression("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")
    assert expr.magnitude() == 3488.0
