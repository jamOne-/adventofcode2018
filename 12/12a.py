import re
import sys


GENERATIONS = 20
OFFSET = 50
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


def solve(puzzle_input):
  lines = list(puzzle_input)
  pots = init_pots_with(lines[0].strip().split(' ')[-1])
  patterns = dict()

  for line in lines[2:]:
    pattern, product = pattern_re.match(line).groups()
    patterns[pattern] = product

  for generation in range(GENERATIONS):
    pots = run_generation(pots, patterns)

  result = 0
  for i in range(len(pots)):
    if pots[i] == '#':
      result += i - OFFSET

  return result


print(solve(sys.stdin))
