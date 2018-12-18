import re
import sys
import argparse
from itertools import chain

parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="debug", action="store_true")
args = parser.parse_args()

line_re = re.compile('([xy])=(\d+), ([xy])=(\d+)..(\d+)')
SINK = 500, 0


def parse_input(puzzle_input):
  lines = list(puzzle_input)
  clay = set()

  for line in lines:
    a, value, b, begin, end = line_re.match(line).groups()
    value, begin, end = tuple(map(int, (value, begin, end)))

    xs = range(begin, end + 1) if b == 'x' else [value]
    ys = range(begin, end + 1) if b == 'y' else [value]

    for x in xs:
      for y in ys:
        clay.add((x, y))

  return clay


def flow(clay, still_water, visited, start):
  x, y = start
  below = x, y + 1
  visited_from_here = set()
  max_y = max(clay, key=lambda xy: xy[1])[1]

  if below not in clay and below not in still_water:
    if below[1] <= max_y:
      visited.add(below)
      visited_from_here.add(below)

      visited_below = flow(clay, still_water, visited, below)
      visited_from_here.update(visited_below)
  else:
    for pos in [(x - 1, y), (x + 1, y)]:
      if pos not in clay and pos not in visited:
        visited.add(pos)
        visited_from_here.add(pos)

        visited_from_pos = flow(clay, still_water, visited, pos)
        visited_from_here.update(visited_from_pos)
  
  if y != max_y and all(map(lambda xy: xy[1] <= y, visited_from_here)):
    still_water.add(start)
  
  return visited_from_here


def get_furthest_visited(visited, step, x, y):
  furthest_x = x

  while (furthest_x, y) in visited:
    furthest_x += step
  
  return furthest_x - step, y


def is_still(visited, x, y):
  last_right = get_furthest_visited(visited, 1, x, y)
  last_left = get_furthest_visited(visited, -1, x, y)

  return all(map(lambda xy: (xy[0], xy[1] + 1) not in visited, [(x, y), last_left, last_right]))


def drop(clay, still_water, start):
  max_y = max(clay, key=lambda xy: xy[1])[1]
  visited = set()
  stack = [start]

  while stack:
    x, y = stack.pop()
    below = x, y + 1

    if below not in clay and below not in still_water:
      if below not in visited and below[1] <= max_y:
        visited.add(below)
        stack.append(below)
    else:
      for pos in [(x - 1, y), (x + 1, y)]:
        if pos not in visited and pos not in clay and pos not in still_water:
          visited.add(pos)
          stack.append(pos)
  
  for x, y in visited:
    if y < max_y and is_still(visited, x, y):
      still_water.add((x, y))

  return visited


def draw(clay, still_water, visited):
  min_x, max_x = min(chain(visited, clay, still_water), key=lambda xy: xy[0])[0], max(chain(visited, clay, still_water), key=lambda xy: xy[0])[0]
  min_y, max_y = min(clay, key=lambda xy: xy[1])[1], max(clay, key=lambda xy: xy[1])[1]

  for y in range(min_y, max_y + 1):
    row = ''

    for x in range(min_x, max_x + 1):
      if (x, y) in clay:
        row += '#'
      elif (x, y) in still_water:
        row += '~'
      elif (x, y) in visited:
        row += '|'
      else:
        row += '.'
    
    print(row)


def solve(puzzle_input):
  clay = parse_input(puzzle_input)
  still_water, visited = set(), set()
  still_water_length = -1

  while len(still_water) != still_water_length:
    still_water_length = len(still_water)
    visited = drop(clay, still_water, SINK)

  if args.debug:  
    draw(clay, still_water, visited)

  min_y, max_y = min(clay, key=lambda xy: xy[1])[1], max(clay, key=lambda xy: xy[1])[1]
  valid_visited = set(filter(lambda xy: min_y <= xy[1] <= max_y, chain(visited, still_water)))

  return len(valid_visited)


print(solve(sys.stdin))
