import sys
from collections import defaultdict

MAX_SIZE = 400
INF = 999999
SAFE_DIST = 10000


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_manhattans(points, dest_point):
    return sum(map(lambda point: manhattan(point, dest_point), points))


def get_safe_points(points):
    for x in range(MAX_SIZE):
        for y in range(MAX_SIZE):
            if get_manhattans(points, (x, y)) < SAFE_DIST:
                yield x, y


def get_neighbours(point):
    x, y = point
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def solve(lines):
    points = list(map(lambda line: tuple(map(int, line.split(', '))), lines))
    safe_points = set(get_safe_points(points))
    return len(safe_points)


print(solve(sys.stdin))
