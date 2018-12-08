import sys
import re
import heapq
from collections import defaultdict

MAX_IN_QUEUE = 5

line_re = re.compile('^Step (.+) must.*step (.+) can begin.$')


def get_starting_nodes(ins):
    for node, in_count in ins.items():
        if in_count == 0:
            yield node


def insert_as_much_as_possible(time, queue, nodes):
    nodes.sort(reverse=True)

    while len(queue) < MAX_IN_QUEUE and len(nodes) > 0:
        node = nodes.pop()
        heapq.heappush(queue, (time + 61 + ord(node) - ord('A'), node))


def solve(lines):
    nodes = defaultdict(list)
    ins = defaultdict(int)

    for line in lines:
        u, v = line_re.match(line).groups()
        nodes[u].append(v)
        ins[u] = ins[u]
        ins[v] += 1

    current_time = 0
    waiting_nodes = list(get_starting_nodes(ins))
    queue = []

    insert_as_much_as_possible(current_time, queue, waiting_nodes)

    while queue:
        time, node = heapq.heappop(queue)
        current_time = time

        for neighbour in nodes[node]:
            ins[neighbour] -= 1

            if ins[neighbour] == 0:
                waiting_nodes.append(neighbour)

        insert_as_much_as_possible(current_time, queue, waiting_nodes)

    return current_time


print(solve(sys.stdin))
