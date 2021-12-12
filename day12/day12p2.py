import re
from collections import defaultdict, Counter
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


def find_all_paths3(graph, start, end, path=None):
    #    print(f"checking {start} -> {end} with {path}")
    if not path:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        # Count up number of times this node is already in the path
        existing_node_count = sum([1 for _ in path if _ == node])
        # Figure out if any other small caves have been traversed
        # multiple times in the existing path
        small_cave_counter = Counter(
            [_ for _ in path if (_.lower() == _) and (_ != node)]
        )
        # Only care if there is one with a count > 1
        other_double_small_caves = (
            small_cave_counter.most_common(1)
            and small_cave_counter.most_common(1)[0][1] > 1
        )
        # Resaons that are valid to travserse a child node:
        #    1) it's not already in the path
        #    2) it's a large cave (can visit unlimited number of times)
        #    3) it's a small cave we have visited once before as long
        #       as we have not visited any other small cave more than once
        if (
            (node not in path)
            or (node.upper() == node)
            or ((existing_node_count == 1) and (not other_double_small_caves))
        ):
            newpaths = find_all_paths3(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


graph = defaultdict(set)

with open("input.txt") as input:
    for line in input.readlines():
        nodes = parse_line(line.strip())
        # To prevent multi passes through "end" or "start" we
        # only add outbound links from "start" and
        # only inbout links to "end"
        if nodes[1] == "start":
            graph[nodes[1]].add(nodes[0])
        elif nodes[0] == "end":
            graph[nodes[1]].add(nodes[0])
        else:
            graph[nodes[0]].add(nodes[1])
            if (nodes[0] != "start") and (nodes[1] != "end"):
                graph[nodes[1]].add(nodes[0])

pp.pprint(graph)

all_paths = find_all_paths3(graph, "start", "end")
# pp.pprint(all_paths)
print(f"total paths = {len(all_paths)}")
