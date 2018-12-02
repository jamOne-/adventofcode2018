import sys
from collections import Counter


def solve(lines):
    twos, threes = 0, 0

    for box in lines:
        letters = Counter(box)
        count_two, count_three = False, False

        for letter, count in letters.items():
            if count == 2:
                count_two = True
            elif count == 3:
                count_three = True

        if count_two:
            twos += 1
        if count_three:
            threes += 1

    return twos * threes


print(solve(sys.stdin))
