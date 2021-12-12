import re
from collections import defaultdict
import pprint

pp = pprint.PrettyPrinter(indent=4)


def parse_line(l: str) -> tuple:
    # Use https://pythex.org/
    m = re.match(r"(\w*)-(\w*)", l)
    if not m:
        raise ValueError(f'The input string "{l}" does not match the expected pattern')
    return m.groups()


# From https://www.python.org/doc/essays/graphs/
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_all_paths2(graph, start, end, path=[]):
    #    print(f"checking {start} -> {end} with {path}")
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if (node not in path) or (node.upper() == node):
            newpaths = find_all_paths2(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


graph = defaultdict(set)

with open("input.txt") as input:
    for line in input.readlines():
        nodes = parse_line(line.strip())
        graph[nodes[0]].add(nodes[1])
        graph[nodes[1]].add(nodes[0])

pp.pprint(graph)

all_paths = find_all_paths2(graph, "start", "end")
# pp.pprint(all_paths)
print(f"total paths = {len(all_paths)}")
