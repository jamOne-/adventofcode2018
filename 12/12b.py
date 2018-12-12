import re
import sys


GENERATIONS = 50000000000
OFFSET = 1000
pattern_re = re.compile('(.{5}) => (.)')


def init_pots_with(pots):
  return '.' * OFFSET + pots + '.' * OFFSET


def run_generation(pots, patterns):
  next_generation = ''

  for i in range(2, len(pots) - 2):
    pattern = pots[i - 2:i + 3]
    next_generation += patterns[pattern]
  
  next_generation = '..' + next_generation + '..'

  return next_generation 


def sum_pots(pots):
  result = 0
  for i in range(len(pots)):
    if pots[i] == '#':
      result += i - OFFSET

  return result


def solve(puzzle_input):
  lines = list(puzzle_input)
  pots = init_pots_with(lines[0].strip().split(' ')[-1])
  patterns = dict()

  for line in lines[2:]:
    pattern, product = pattern_re.match(line).groups()
    patterns[pattern] = product

  last_sum, last_diff = 0, 0

  for generation in range(GENERATIONS):
    pots = run_generation(pots, patterns)
    pots_sum = sum_pots(pots)
    diff = pots_sum - last_sum

    if diff == last_diff:
      generations_remaining = GENERATIONS - 1 - generation
      return pots_sum + generations_remaining * diff
    else:
      last_sum, last_diff = pots_sum, diff


print(solve(sys.stdin))
