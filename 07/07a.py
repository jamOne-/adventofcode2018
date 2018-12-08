import sys
import re
from collections import defaultdict

line_re = re.compile('^Step (.+) must.*step (.+) can begin.$')


def get_starting_nodes(ins):
    for node, in_count in ins.items():
        if in_count == 0:
            yield node


def solve(lines):
    nodes = defaultdict(list)
    ins = defaultdict(int)

    for line in lines:
        u, v = line_re.match(line).groups()
        nodes[u].append(v)
        ins[u] = ins[u]
        ins[v] += 1

    result = ''
    ready_nodes = sorted(get_starting_nodes(ins), reverse=True)

    while ready_nodes:
        node = ready_nodes.pop()
        result += node

        for neighbour in nodes[node]:
            ins[neighbour] -= 1

            if ins[neighbour] == 0:
                ready_nodes.append(neighbour)
                ready_nodes = sorted(ready_nodes, reverse=True)

    return result


print(solve(sys.stdin))
