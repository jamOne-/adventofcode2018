import sys


def solve(lines):
    return sum(map(int, lines))


print(solve(sys.stdin))
