import sys
from collections import namedtuple

CART_CHARS = ['^', '>', 'v', '<']
TURN_CHARS = ['/', '\\']
INTERSECTION = '+'
MOVES = { '<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1) }

Cart = namedtuple('Cart', ['position', 'direction', 'state'])


def parse_input(puzzle_input):
  mine = []
  carts = dict()

  for y, line in enumerate(puzzle_input):
    row = ''

    for x, char in enumerate(line):
      if char in CART_CHARS:
        direction = char
        cart = Cart((x, y), direction, 0)
        carts[x, y] = cart

        char = '-'

        if direction == '^' or direction == 'v':
          char = '|'
        
      row += char
    
    mine.append(row)
  
  return mine, carts


def handle_curve(curve, direction):
  if curve == '/':
    if direction == '^': return '>'
    if direction == '>': return '^'
    if direction == 'v': return '<'
    if direction == '<': return 'v'

  if curve == '\\':
    if direction == '^': return '<'
    if direction == '>': return 'v'
    if direction == 'v': return '>'
    if direction == '<': return '^'


def turn(direction, delta):
  direction_index = CART_CHARS.index(direction)
  return CART_CHARS[(direction_index + delta) % 4]


def handle_intersection(direction, state):
  if state == 0: return turn(direction, -1), 1
  if state == 1: return direction, 2
  if state == 2: return turn(direction, 1), 0


def tick(mine, carts):
  for (x, y), direction, state in sorted(carts.values(), key=lambda cart: (cart.position[1], cart.position[0])):
    char = mine[y][x]

    if char in TURN_CHARS:
      direction = handle_curve(char, direction)
    elif char == INTERSECTION:
      direction, state = handle_intersection(direction, state)
    
    move = MOVES[direction]
    new_x, new_y = x + move[0], y + move[1]

    if (new_x, new_y) in carts:
      return new_x, new_y
    
    carts[new_x, new_y] = Cart((new_x, new_y), direction, state)
    del carts[x, y]
  
  return None


def solve(puzzle_input):
  mine, carts = parse_input(puzzle_input)
  crashed = None

  while not crashed:
    crashed = tick(mine, carts)
  
  return crashed


print(solve(sys.stdin))
