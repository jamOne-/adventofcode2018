import sys


def react(polymer):
    result = ''

    for c in polymer:
        if len(result) == 0 or result[-1].swapcase() != c:
            result += c
        else:
            result = result[:-1]

    return len(result)


def solve(polymer):
    units = set(polymer.lower())
    best_result = 999999

    for unit in units:
        new_polymer = polymer.replace(unit, '').replace(unit.upper(), '')
        best_result = min(best_result, react(new_polymer))

    return best_result


print(solve(sys.stdin.readline().strip()))
