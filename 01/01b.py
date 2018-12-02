import sys
from itertools import cycle


def solve(lines):
    freqChanges = cycle(map(int, lines))
    frequencies = set([0])
    frequency = 0

    for freqChange in freqChanges:
        frequency += freqChange

        if frequency in frequencies:
            return frequency
        else:
            frequencies.add(frequency)


print(solve(sys.stdin))
