import sys

def parse_input(puzzle_input):
  return [line.strip() for line in puzzle_input]


def get_neighbours(fields, x, y):
  max_x, max_y = len(fields[0]), len(fields)

  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      new_x, new_y = x + dx, y + dy

      if 0 <= new_x < max_x and 0 <= new_y < max_y and (new_x, new_y) != (x, y):
        yield fields[new_y][new_x]


def tick(fields):
  updated_fields = []
  max_x, max_y = len(fields[0]), len(fields)

  for y in range(max_y):
    row = ''

    for x in range(max_x):
      field = fields[y][x]
      neighbours = ''.join(get_neighbours(fields, x, y))

      if field == '.' and neighbours.count('|') >= 3:
        field = '|'
      elif field == '|' and neighbours.count('#') >= 3:
        field = '#'
      elif field == '#' and (neighbours.count('#') == 0 or neighbours.count('|') == 0):
        field = '.'
      
      row += field

    updated_fields.append(row)
  
  return updated_fields


def solve(puzzle_input):
  fields = parse_input(puzzle_input)

  for minute in range(10):
    fields = tick(fields)

  return sum(map(lambda row: row.count('|'), fields)) * sum(map(lambda row: row.count('#'), fields))


print(solve(sys.stdin))
