import sys
import re


def solve(lines):
    line_re = re.compile('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')
    squares = set()
    common_squares = set()

    for line in lines:
        box_id, pos_x, pos_y, width, height = map(
            int,
            line_re.match(line).groups()
        )

        for x in range(pos_x, pos_x + width):
            for y in range(pos_y, pos_y + height):
                if (x, y) in squares:
                    common_squares.add((x, y))
                else:
                    squares.add((x, y))

    return len(common_squares)


print(solve(sys.stdin))
