import sys
from collections import defaultdict

MAX_SIZE = 400
INF = 999999


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_closest(points, dest_point):
    closest, min_dist = None, INF

    for i, point in enumerate(points):
        dist = manhattan(point, dest_point)

        if dist < min_dist:
            closest, min_dist = i, dist
        elif dist == min_dist:
            closest = None

    return closest


def is_good_candidate(points, i):
    for x in range(MAX_SIZE):
        for y in [0, MAX_SIZE - 1]:
            if get_closest(points, (x, y)) == i:
                return False

    for x in [0, MAX_SIZE - 1]:
        for y in range(MAX_SIZE):
            if get_closest(points, (x, y)) == i:
                return False

    return True


def get_candidates(points):
    return list(filter(lambda i: is_good_candidate(points, i), range(len(points))))


def solve(lines):
    counts = defaultdict(int)
    points = list(map(lambda line: tuple(map(int, line.split(', '))), lines))
    candidates = get_candidates(points)

    for x in range(MAX_SIZE):
        for y in range(MAX_SIZE):
            closest = get_closest(points, (x, y))

            if closest != None:
                counts[closest] += 1

    return counts[max(candidates, key=lambda id: counts[id])]


print(solve(sys.stdin))
