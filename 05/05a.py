import sys


def solve(polymer):
    result = ''

    for c in polymer:
        if len(result) == 0 or result[-1].swapcase() != c:
            result += c
        else:
            result = result[:-1]

    return len(result)


print(solve(sys.stdin.readline().strip()))
