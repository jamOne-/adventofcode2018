import re
import sys


def get_all_numbers(string):
  return re.findall('\d+', string)


def prepare_cave(target, depth):
  cols, rows = target[0] + 1, target[1] + 1
  cave = [[0] * cols for row in range(rows)]

  for x in range(1, cols):
    cave[0][x] = (x * 16807 + depth) % 20183
  
  for y in range(1, rows):
    cave[y][0] = (y * 48271 + depth) % 20183
  
  for y in range(1, rows):
    for x in range(1, cols):
      cave[y][x] = (cave[y][x - 1] * cave[y - 1][x] + depth) % 20183
  
  cave[0][0] = depth % 20183
  cave[target[1]][target[0]] = depth % 20183

  cave = [list(map(lambda region: region % 3, row)) for row in cave]

  return cave


def draw(cave):
  for cave_row in cave:
    row = ''

    for region in cave_row:
      if region == 0:
        row += '.'
      elif region == 1:
        row += '='
      elif region == 2:
        row += '|'
      else:
        print("WTF")
    
    print(row)


def solve(puzzle_input):
  lines = list(puzzle_input)
  depth = int(get_all_numbers(lines[0])[0])
  target = tuple(map(int, get_all_numbers(lines[1])))
  cave = prepare_cave(target, depth)

  # draw(cave)
  return sum([sum(row) for row in cave])


print(solve(sys.stdin))
