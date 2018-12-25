import re
import sys


def get_all_numbers(line):
  return tuple(map(int, re.findall('-?\d+', line)))


def distance(point1, point2):
  return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + abs(point1[2] - point2[2]) + abs(point1[3] - point2[3])


def get_connections(points):
  connections = [[] for _ in points]

  for i, point in enumerate(points):
    for j in range(i + 1, len(points)):
      point2 = points[j]

      if distance(point, point2) <= 3:
        connections[i].append(j)
        connections[j].append(i)
  
  return connections


def get_number_of_constelations(connections):
  visited = set()
  stack = []
  counter = 0

  for i in range(len(connections)):
    if i in visited:
      continue

    visited.add(i)
    stack = [i]
    counter += 1

    while stack:
      u = stack.pop()

      for v in connections[u]:
        if v not in visited:
          visited.add(v)
          stack.append(v)
  
  return counter


def solve(puzzle_input):
  points = [get_all_numbers(line) for line in puzzle_input]
  connections = get_connections(points)

  return get_number_of_constelations(connections)


print(solve(sys.stdin))
