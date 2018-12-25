import re
import sys
from collections import namedtuple

Nanobot = namedtuple('Nanobot', ['x', 'y', 'z', 'r'])


def get_numbers(string):
  return tuple(map(int, re.findall('-?\d+', string)))


def parse_input(puzzle_input):
  return [Nanobot(*get_numbers(line)) for line in puzzle_input]


def count_in_range(nanobots, strongest):
  counter = 0

  for x, y, z, r in nanobots:
    if abs(x - strongest.x) + abs(y - strongest.y) + abs(z - strongest.z) <= strongest.r:
      counter += 1
  
  return counter


def solve(puzzle_input):
  nanobots = parse_input(puzzle_input)
  strongest = max(nanobots, key=lambda nanobot: nanobot.r)

  return count_in_range(nanobots, strongest)


print(solve(sys.stdin))
