import sys
import re
from collections import defaultdict

line_re = re.compile('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')


def parse_lines(lines):
    return [tuple(map(int, line_re.match(line).groups())) for line in lines]


def check_claim(squares, claim):
    box_id, pos_x, pos_y, width, height = claim

    for x in range(pos_x, pos_x + width):
        for y in range(pos_y, pos_y + height):
            if squares[x, y] != 1:
                return False

    return True


def solve(lines):
    squares = defaultdict(int)
    claims = parse_lines(lines)

    for box_id, pos_x, pos_y, width, height in claims:
        for x in range(pos_x, pos_x + width):
            for y in range(pos_y, pos_y + height):
                squares[x, y] += 1

    for claim in claims:
        if check_claim(squares, claim):
            return claim[0]


print(solve(sys.stdin))
