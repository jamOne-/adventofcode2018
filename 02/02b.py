import sys
from functools import reduce
from collections import Counter


def update_diff(diff, letters):
    diffs, common = diff
    let1, let2 = letters

    if let1 == let2:
        return diffs, common + let1
    else:
        return diffs + 1, common


def get_diff(box1, box2):
    return reduce(
        update_diff,
        zip(box1, box2),
        (0, '')
    )


def solve(lines):
    boxes = list(lines)

    for i in range(0, len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            diffs, common = get_diff(boxes[i], boxes[j])

            if diffs == 1:
                return common


print(solve(sys.stdin))
