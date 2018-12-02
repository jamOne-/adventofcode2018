import sys


def solve(lines):
    return sum(map(int, lines))


lines = []

for line in sys.stdin:
    lines.append(line)


print(solve(lines))
