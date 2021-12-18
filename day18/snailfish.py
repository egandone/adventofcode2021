from math import floor, ceil


class ExprNode:
    left = right = None
    parent = None

    def get_nodes(self) -> list:
        all_nodes = []
        if type(self.left) != int:
            all_nodes.extend(self.left.get_nodes())
        all_nodes.append(self)
        if type(self.right) != int:
            all_nodes.extend(self.right.get_nodes())
        return all_nodes

    def depth(self) -> int:
        if self.parent:
            return 1 + self.parent.depth()
        else:
            return 0

    def contains_num(self) -> bool:
        return type(self.right) == int or type(self.left) == int

    def add_left_first(self, n):
        if type(self.left) == int:
            self.left += n
        elif type(self.right) == int:
            self.right += n

    def add_right_first(self, n):
        if type(self.right) == int:
            self.right += n
        elif type(self.left) == int:
            self.left += n

    def add(self, other_expr):
        new_expr = ExprNode()
        new_expr.left = self
        new_expr.right = other_expr
        self.parent = other_expr.parent = new_expr
        return new_expr

    def magnitude(self):
        if type(self.left) == int:
            left_value = self.left
        else:
            left_value = self.left.magnitude()
        if type(self.right) == int:
            right_value = self.right
        else:
            right_value = self.right.magnitude()
        magnitude = 3 * left_value + 2 * right_value
        return magnitude

    def __str__(self):
        return f"[{self.left},{self.right}]"

    def __repr__(self):
        return f"[{self.left},{self.right}]"


def split_string(s: str) -> tuple:
    depth = 0
    split_point = None
    c = 0
    while c < len(s) and not split_point:
        if s[c] == "[":
            depth += 1
        elif s[c] == "]":
            depth -= 1
        elif s[c] == "," and depth == 1:
            split_point = c
        c += 1

    return (s[1:split_point], s[split_point + 1 : -1])


def parse_expression(s: str) -> ExprNode:
    (left, right) = split_string(s)
    node = ExprNode()
    if left.isdigit() == 1:
        node.left = int(left)
    else:
        node.left = parse_expression(left)
        node.left.parent = node
    if right.isdigit() == 1:
        node.right = int(right)
    else:
        node.right = parse_expression(right)
        node.right.parent = node
    return node


def reduce(root: ExprNode) -> ExprNode:
    changed = True
    while changed:
        changed = False
        nodes = root.get_nodes()
        i = 0
        while i < len(nodes) and not changed:
            node = nodes[i]
            if node.depth() == 4:
                changed = True
                if i > 0:
                    j = i - 1
                    while not nodes[j].contains_num():
                        j -= 1
                    nodes[j].add_right_first(node.left)
                if i < len(nodes) - 1:
                    j = i + 1
                    while not nodes[j].contains_num():
                        j += 1
                    nodes[j].add_left_first(node.right)
                if node.parent.right == node:
                    node.parent.right = 0
                else:
                    node.parent.left = 0
            i += 1
        if not changed:
            i = 0
            while not changed and i < len(nodes):
                node = nodes[i]
                if type(node.left) == int and node.left >= 10:
                    new_left = floor(node.left / 2.0)
                    new_right = ceil(node.left / 2.0)
                    node.left = ExprNode()
                    node.left.left = new_left
                    node.left.right = new_right
                    node.left.parent = node
                    changed = True
                elif type(node.right) == int and node.right >= 10:
                    new_left = floor(node.right / 2.0)
                    new_right = ceil(node.right / 2.0)
                    node.right = ExprNode()
                    node.right.left = new_left
                    node.right.right = new_right
                    node.right.parent = node
                    changed = True
                i += 1

    return root
